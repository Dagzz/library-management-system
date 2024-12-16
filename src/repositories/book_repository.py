from src.models.book import Book
from src.dal.database_connection import get_session
from typing import List

class BookRepository:
    def __init__(self):
        """
        Initialize the BookRepository class.

        This constructor sets up the database session for the repository 
        by using the `get_session` function from the `database_connection` module.

        :return: None
        """
        self.session = get_session()

    def add_book(self, book: Book) -> Book:
        """
        Add a new book to the database.

        This function takes a `Book` object as input, adds it to the current session,
        commits the transaction to persist the data in the database, and returns the added book.

        :param book: A `Book` object to be added to the database.
        :return: The `Book` object that was added to the database.
        """
        self.session.add(book)
        self.session.commit()
        return book

    def get_all_books(self) -> List[Book]:
        """
        Retrieve all books from the database.

        This function queries the `Book` table to fetch all the records and 
        returns them as a list of `Book` objects.

        :return: A list of `Book` objects representing all books in the database.
        """
        return self.session.query(Book).all()

    def get_book_by_id(self, book_id: int) -> (Book | None):
        """
        Retrieve a specific book from the database by its ID.

        This function filters the `Book` table by the given `book_id` 
        and returns the first matching `Book` object, or `None` if no match is found.

        :param book_id: An integer representing the ID of the book to retrieve.
        :return: A `Book` object if found, or `None` if no book matches the given ID.
        """
        return self.session.query(Book).filter_by(id_book=book_id).first()

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book from the database by its ID.

        This function retrieves a `Book` object by its ID, deletes it from the 
        current session if it exists, and commits the transaction to apply the changes.

        :param book_id: An integer representing the ID of the book to delete.
        :return: None
        """
        book = self.get_book_by_id(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
