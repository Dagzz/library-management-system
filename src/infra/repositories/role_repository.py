from typing import List, Optional
from src.core.models import Role, User
from src.core.models.associations import user_role_table

class RoleRepository:
    """
    RoleRepository

    Handles database operations related to the Role model.

    Responsibilities:
    - Managing roles in the database, including adding, updating, or deleting roles.
    - Fetching roles by ID or name.
    - Associating roles with users.

    Usage:
    - Initialize with a session factory:
        repo = RoleRepository(get_session)
    - Use the provided methods to perform CRUD operations and retrieve role data.
    """
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def get_role_by_id(self, role_id: int) -> Optional[Role]:
        """
        Fetch a role by its ID.
        """
        session = self.session_factory()
        try:
            return session.query(Role).filter(Role.id_role == role_id).one_or_none()
        finally:
            session.close()

    def get_role_by_name(self, role_name: str) -> Optional[Role]:
        """
        Fetch a role by its name (case insensitive).
        """
        session = self.session_factory()
        try:
            return session.query(Role).filter(Role.role_name.ilike(f"%{role_name}%")).one_or_none()
        finally:
            session.close()

    def get_all_roles(self) -> List[Role]:
        """
        Fetch all roles in the database.
        """
        session = self.session_factory()
        try:
            return session.query(Role).all()
        finally:
            session.close()

    def get_users_with_role(self, role_id: int) -> List[User]:
        """
        Fetch all users associated with a specific role.
        """
        session = self.session_factory()
        try:
            role = session.query(Role).filter(Role.id_role == role_id).one_or_none()
            return role.users if role else []
        finally:
            session.close()

    def add_role(self, role: Role) -> Role:
        """
        Add a new role to the database.
        """
        session = self.session_factory()
        try:
            session.add(role)
            session.commit()
            return role
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def update_role(self, role: Role) -> Role:
        """
        Update an existing role's details.
        """
        session = self.session_factory()
        try:
            session.merge(role)
            session.commit()
            return role
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def delete_role(self, role_id: int) -> bool:
        """
        Delete a role by its ID.
        """
        session = self.session_factory()
        try:
            role = session.query(Role).filter(Role.id_role == role_id).one_or_none()
            if role:
                session.delete(role)
                session.commit()
                return True
            return False
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_user_roles(self, user_id: int) -> List[str]:
        """
        Retrieve the list of role names for a given user.

        Args:
            user_id (int): The ID of the user whose roles are to be retrieved.

        Returns:
            List[str]: A list of role names associated with the user.
        """
        session = self.session_factory()
        try:
            roles = (
                session.query(Role.role_name)
                .join(user_role_table, Role.id_role == user_role_table.c.id_role)
                .filter(user_role_table.c.id_user == user_id)
                .all()
            )
            return [role.role_name for role in roles]
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
