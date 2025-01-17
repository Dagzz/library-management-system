from sqlalchemy.orm import Session
from typing import List, Optional
from src.models import Modification

class ModificationRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_modification_by_id(self, modification_id: int) -> Optional[Modification]:
        """
        Fetch a modification by its ID.
        """
        return self.session.query(Modification).filter(Modification.id_modif == modification_id).one_or_none()

    def get_modifications_by_book(self, book_id: int) -> List[Modification]:
        """
        Fetch all modifications associated with a specific book.
        """
        return self.session.query(Modification).filter(Modification.id_book == book_id).all()

    def get_modifications_by_user(self, user_id: int) -> List[Modification]:
        """
        Fetch all modifications made by a specific user.
        """
        return self.session.query(Modification).filter(Modification.id_user == user_id).all()

    def get_all_modifications(self) -> List[Modification]:
        """
        Fetch all modifications in the database.
        """
        return self.session.query(Modification).all()

    def add_modification(self, modification: Modification) -> Modification:
        """
        Add a new modification to the database.
        """
        self.session.add(modification)
        self.session.commit()
        return modification

    def update_modification(self, modification: Modification) -> Modification:
        """
        Update an existing modification's details.
        """
        self.session.merge(modification)
        self.session.commit()
        return modification

    def delete_modification(self, modification_id: int) -> bool:
        """
        Delete a modification by its ID.
        """
        modification = self.get_modification_by_id(modification_id)
        if modification:
            self.session.delete(modification)
            self.session.commit()
            return True
        return False
