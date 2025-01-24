from datetime import datetime
from sqlalchemy.exc import NoResultFound
from typing import Optional, List
from src.core.models import User, Role, Address, Reservation

class UserRepository:
    """
        UserRepository

        Handles database operations related to the User model.

        Responsibilities:
        - Managing user records, including adding, updating, deleting, and retrieving users.
        - Fetching users by various attributes such as ID, email, or username.
        - Supporting advanced queries for user-related data, such as filtering by status or activity.

        Usage:
        - Initialize with a session factory:
            repo = UserRepository(get_session)
        - Use the provided methods to perform CRUD operations and retrieve user data.
    """
    def __init__(self, session_factory):
        """
        Initialize the repository with a session factory.
        
        Args:
            session_factory: A callable that returns a new SQLAlchemy session.
        """
        self.session_factory = session_factory

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Fetch a user by their ID.
        """
        session = self.session_factory()
        try:
            return session.query(User).filter(User.id_user == user_id).one()
        except NoResultFound:
            return None
        finally:
            session.close()

    def get_user_by_login(self, login: str) -> Optional[User]:
        """
        Fetch a user by their login.
        """
        session = self.session_factory()
        try:
            return session.query(User).filter(User.login == login).one()
        except NoResultFound:
            return None
        finally:
            session.close()

    def get_all_users(self) -> List[User]:
        """
        Fetch all users.
        """
        session = self.session_factory()
        try:
            return session.query(User).all()
        finally:
            session.close()

    def get_users_by_role(self, role_name: str) -> List[User]:
        """
        Fetch users by their role.
        """
        session = self.session_factory()
        try:
            return (
                session.query(User)
                .join(User.roles)
                .filter(Role.role_name == role_name)
                .all()
            )
        finally:
            session.close()

    def get_users_by_reservation_status(self, is_confirmed: bool) -> List[User]:
        """
        Fetch users who have reservations with the given status.
        """
        session = self.session_factory()
        try:
            return (
                session.query(User)
                .join(User.reservations)
                .filter(Reservation.is_confirmed == is_confirmed)
                .all()
            )
        finally:
            session.close()

    def add_user(self, user: User) -> User:
        """
        Add a new user to the database.
        """
        session = self.session_factory()
        try:
            session.add(user)
            session.commit()
            return user
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def update_user(self, user: User) -> User:
        """
        Update an existing user's information.
        """
        session = self.session_factory()
        try:
            session.merge(user)
            session.commit()
            return user
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by their ID.
        """
        session = self.session_factory()
        try:
            user = session.query(User).filter(User.id_user == user_id).one_or_none()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_users_by_address_city(self, city_name: str) -> List[User]:
        """
        Fetch users based on their city's name.
        """
        session = self.session_factory()
        try:
            return (
                session.query(User)
                .join(User.address)
                .join(Address.city)
                .filter(Address.city.has(name=city_name))
                .all()
            )
        finally:
            session.close()

    def update_last_connection_date(self, user_id: int) -> bool:
        """
        Update the last connection date of a user to the current datetime.

        Args:
            user_id (int): The ID of the user to update.

        Returns:
            bool: True if the update was successful, False if the user was not found.
        """
        session = self.session_factory()
        try:
            user = session.query(User).filter(User.id_user == user_id).one_or_none()
            if user:
                user.last_connection_date = datetime.now()
                session.commit()
                return True
            return False
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
