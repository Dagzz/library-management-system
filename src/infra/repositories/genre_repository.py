"""
GenreRepository

Handles database operations related to the `Genre` model.

Responsibilities:
- Managing genre-related data.
- Fetching genre records by ID or name.
- Querying genres associated with specific books or criteria.
- Creating, updating, or deleting genre records.

Usage:
- Initialize with a session factory:
    repo = GenreRepository(get_session)
- Use the provided methods to interact with the database for genre-related operations.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from src.core.models import Genre, Book

class GenreRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_genre_by_id(self, genre_id: int) -> Optional[Genre]:
        """
        Fetch a genre by its ID.
        """
        return self.session.query(Genre).filter(Genre.id_genre == genre_id).one_or_none()

    def get_genre_by_name(self, name: str) -> Optional[Genre]:
        """
        Fetch a genre by its name (case insensitive).
        """
        return self.session.query(Genre).filter(Genre.name_genre.ilike(f"%{name}%")).one_or_none()

    def get_all_genres(self) -> List[Genre]:
        """
        Fetch all genres in the database.
        """
        return self.session.query(Genre).all()

    def get_books_in_genre(self, genre_id: int) -> List[Book]:
        """
        Fetch all books associated with a specific genre.
        """
        genre = self.get_genre_by_id(genre_id)
        return genre.books if genre else []

    def add_genre(self, genre: Genre) -> Genre:
        """
        Add a new genre to the database.
        """
        self.session.add(genre)
        self.session.commit()
        return genre

    def update_genre(self, genre: Genre) -> Genre:
        """
        Update an existing genre's details.
        """
        self.session.merge(genre)
        self.session.commit()
        return genre

    def delete_genre(self, genre_id: int) -> bool:
        """
        Delete a genre by its ID.
        """
        genre = self.get_genre_by_id(genre_id)
        if genre:
            self.session.delete(genre)
            self.session.commit()
            return True
        return False
