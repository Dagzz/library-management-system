from sqlalchemy.orm import Session
from typing import List, Optional
from models import Book, Author, Genre, Reservation

class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Fetch a book by its ID.
        """
        return self.session.query(Book).filter(Book.id_book == book_id).one_or_none()

    def get_books_by_title(self, title: str) -> List[Book]:
        """
        Fetch books by their title (case insensitive).
        """
        return self.session.query(Book).filter(Book.title.ilike(f"%{title}%")).all()

    def get_books_by_author(self, author_id: int) -> List[Book]:
        """
        Fetch all books by a specific author.
        """
        return (
            self.session.query(Book)
            .join(Book.authors)
            .filter(Author.id_author == author_id)
            .all()
        )

    def get_books_by_genre(self, genre_id: int) -> List[Book]:
        """
        Fetch all books in a specific genre.
        """
        return (
            self.session.query(Book)
            .join(Book.genres)
            .filter(Genre.id_genre == genre_id)
            .all()
        )

    def get_books_by_collection(self, collection_id: int) -> List[Book]:
        """
        Fetch all books in a specific collection.
        """
        return self.session.query(Book).filter(Book.id_collection == collection_id).all()

    def get_books_by_language(self, language_id: int) -> List[Book]:
        """
        Fetch all books in a specific language.
        """
        return self.session.query(Book).filter(Book.id_language == language_id).all()

    def get_books_by_status(self, status: str) -> List[Book]:
        """
        Fetch all books by their status (e.g., "available", "borrowed", "reserved").
        """
        return self.session.query(Book).filter(Book.status == status).all()

    def get_books_by_aspect(self, aspect: str) -> List[Book]:
        """
        Fetch all books by their aspect (e.g., "new", "good", "damaged").
        """
        return self.session.query(Book).filter(Book.aspect == aspect).all()

    def get_reserved_books(self) -> List[Book]:
        """
        Fetch all books that are currently reserved.
        """
        return (
            self.session.query(Book)
            .join(Book.reservations)
            .filter(Reservation.is_confirmed == True)
            .all()
        )

    def add_book(self, book: Book) -> Book:
        """
        Add a new book to the database.
        """
        self.session.add(book)
        self.session.commit()
        return book

    def update_book(self, book: Book) -> Book:
        """
        Update an existing book in the database.
        """
        self.session.merge(book)
        self.session.commit()
        return book

    def delete_book(self, book_id: int) -> bool:
        """
        Delete a book by its ID.
        """
        book = self.get_book_by_id(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
            return True
        return False