from sqlalchemy.orm import Session
from typing import List, Optional
from models import Collection, Book

class CollectionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_collection_by_id(self, collection_id: int) -> Optional[Collection]:
        """
        Fetch a collection by its ID.
        """
        return self.session.query(Collection).filter(Collection.id_collection == collection_id).one_or_none()

    def get_collection_by_name(self, name: str) -> Optional[Collection]:
        """
        Fetch a collection by its name (case insensitive).
        """
        return self.session.query(Collection).filter(Collection.collection_name.ilike(f"%{name}%")).one_or_none()

    def get_all_collections(self) -> List[Collection]:
        """
        Fetch all collections in the database.
        """
        return self.session.query(Collection).all()

    def get_books_in_collection(self, collection_id: int) -> List[Book]:
        """
        Fetch all books in a specific collection.
        """
        collection = self.get_collection_by_id(collection_id)
        return collection.books if collection else []

    def add_collection(self, collection: Collection) -> Collection:
        """
        Add a new collection to the database.
        """
        self.session.add(collection)
        self.session.commit()
        return collection

    def update_collection(self, collection: Collection) -> Collection:
        """
        Update an existing collection's details.
        """
        self.session.merge(collection)
        self.session.commit()
        return collection

    def delete_collection(self, collection_id: int) -> bool:
        """
        Delete a collection by its ID.
        """
        collection = self.get_collection_by_id(collection_id)
        if collection:
            self.session.delete(collection)
            self.session.commit()
            return True
        return False
