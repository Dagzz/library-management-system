from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional
from models import Author, Book

class AuthorRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        """
        Fetch an author by their ID.
        """
        return self.session.query(Author).filter(Author.id_author == author_id).one_or_none()

    def get_authors_by_name(self, name: str) -> List[Author]:
        """
        Fetch authors by their first name, last name, or both (case insensitive).
        """
        return (
            self.session.query(Author)
            .filter(
                (Author.first_name.ilike(f"%{name}%")) | (Author.last_name.ilike(f"%{name}%"))
            )
            .all()
        )

    def get_authors_by_book(self, book_id: int) -> List[Author]:
        """
        Fetch all authors of a specific book.
        """
        return (
            self.session.query(Author)
            .join(Author.books)
            .filter(Book.id_book == book_id)
            .all()
        )

    def get_all_authors(self) -> List[Author]:
        """
        Fetch all authors in the database.
        """
        return self.session.query(Author).all()

    def add_author(self, author: Author) -> Author:
        """
        Add a new author to the database.
        """
        self.session.add(author)
        self.session.commit()
        return author

    def update_author(self, author: Author) -> Author:
        """
        Update an existing author's details.
        """
        self.session.merge(author)
        self.session.commit()
        return author

    def delete_author(self, author_id: int) -> bool:
        """
        Delete an author by their ID.
        """
        author = self.get_author_by_id(author_id)
        if author:
            self.session.delete(author)
            self.session.commit()
            return True
        return False

    def get_authors_with_multiple_books(self) -> List[Author]:
        """
        Fetch authors who have written multiple books.
        """
        return (
            self.session.query(Author)
            .join(Author.books)
            .group_by(Author.id_author)
            .having(func.count(Book.id_book) > 1)
            .all()
        )
