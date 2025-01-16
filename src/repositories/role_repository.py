from sqlalchemy.orm import Session
from typing import List, Optional
from models import Role, User

class RoleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_role_by_id(self, role_id: int) -> Optional[Role]:
        """
        Fetch a role by its ID.
        """
        return self.session.query(Role).filter(Role.id_role == role_id).one_or_none()

    def get_role_by_name(self, role_name: str) -> Optional[Role]:
        """
        Fetch a role by its name (case insensitive).
        """
        return self.session.query(Role).filter(Role.role_name.ilike(f"%{role_name}%")).one_or_none()

    def get_all_roles(self) -> List[Role]:
        """
        Fetch all roles in the database.
        """
        return self.session.query(Role).all()

    def get_users_with_role(self, role_id: int) -> List[User]:
        """
        Fetch all users associated with a specific role.
        """
        role = self.get_role_by_id(role_id)
        return role.users if role else []

    def add_role(self, role: Role) -> Role:
        """
        Add a new role to the database.
        """
        self.session.add(role)
        self.session.commit()
        return role

    def update_role(self, role: Role) -> Role:
        """
        Update an existing role's details.
        """
        self.session.merge(role)
        self.session.commit()
        return role

    def delete_role(self, role_id: int) -> bool:
        """
        Delete a role by its ID.
        """
        role = self.get_role_by_id(role_id)
        if role:
            self.session.delete(role)
            self.session.commit()
            return True
        return False
