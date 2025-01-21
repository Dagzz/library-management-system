"""
LanguageRepository

Handles database operations related to the `Language` model.

Responsibilities:
- Managing language-related data.
- Fetching language records by ID or name.
- Querying languages associated with specific books or other entities.
- Creating, updating, or deleting language records.

Usage:
- Initialize with a session factory:
    repo = LanguageRepository(get_session)
- Use the provided methods to interact with the database for language-related operations.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from src.core.models import Language, Book

class LanguageRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_language_by_id(self, language_id: int) -> Optional[Language]:
        """
        Fetch a language by its ID.
        """
        return self.session.query(Language).filter(Language.id_language == language_id).one_or_none()

    def get_language_by_name(self, name: str) -> Optional[Language]:
        """
        Fetch a language by its name (case insensitive).
        """
        return self.session.query(Language).filter(Language.language_name.ilike(f"%{name}%")).one_or_none()

    def get_all_languages(self) -> List[Language]:
        """
        Fetch all languages in the database.
        """
        return self.session.query(Language).all()

    def get_books_by_language(self, language_id: int) -> List[Book]:
        """
        Fetch all books associated with a specific language.
        """
        language = self.get_language_by_id(language_id)
        return language.books if language else []

    def add_language(self, language: Language) -> Language:
        """
        Add a new language to the database.
        """
        self.session.add(language)
        self.session.commit()
        return language

    def update_language(self, language: Language) -> Language:
        """
        Update an existing language's details.
        """
        self.session.merge(language)
        self.session.commit()
        return language

    def delete_language(self, language_id: int) -> bool:
        """
        Delete a language by its ID.
        """
        language = self.get_language_by_id(language_id)
        if language:
            self.session.delete(language)
            self.session.commit()
            return True
        return False
