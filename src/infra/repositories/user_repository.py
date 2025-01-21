"""
UserRepository

Handles database operations related to the `User` model.

Responsibilities:
- Managing user records, including adding, updating, deleting, and retrieving users.
- Fetching users by various attributes such as ID, email, or username.
- Supporting advanced queries for user-related data, such as filtering by status or activity.

Usage:
- Initialize with a session factory:
    repo = UserRepository(get_session)
- Use the provided methods to perform CRUD operations and retrieve user data.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import Optional, List
from src.core.models import User, Role, Address, Reservation

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Fetch a user by their ID.
        """
        try:
            return self.session.query(User).filter(User.id_user == user_id).one()
        except NoResultFound:
            return None

    def get_user_by_login(self, login: str) -> Optional[User]:
        """
        Fetch a user by their login.
        """
        try:
            return self.session.query(User).filter(User.login == login).one()
        except NoResultFound:
            return None

    def get_all_users(self) -> List[User]:
        """
        Fetch all users.
        """
        return self.session.query(User).all()

    def get_users_by_role(self, role_name: str) -> List[User]:
        """
        Fetch users by their role.
        """
        return (
            self.session.query(User)
            .join(User.roles)
            .filter(Role.role_name == role_name)
            .all()
        )

    def get_users_by_reservation_status(self, is_confirmed: bool) -> List[User]:
        """
        Fetch users who have reservations with the given status.
        """
        return (
            self.session.query(User)
            .join(User.reservations)
            .filter(Reservation.is_confirmed == is_confirmed)
            .all()
        )

    def add_user(self, user: User) -> User:
        """
        Add a new user to the database.
        """
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user: User) -> User:
        """
        Update an existing user's information.
        """
        self.session.merge(user)
        self.session.commit()
        return user

    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by their ID.
        """
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def get_users_by_address_city(self, city_name: str) -> List[User]:
        """
        Fetch users based on their city's name.
        """
        return (
            self.session.query(User)
            .join(User.address)
            .join(Address.city)
            .filter(Address.city.has(name=city_name))
            .all()
        )
