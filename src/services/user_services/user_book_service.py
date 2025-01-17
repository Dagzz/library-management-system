from src.repositories.book_repository import BookRepository
# from repositories.loan_repository import LoanRepository  # if needed
# from models import Book  # import your SQLAlchemy models if needed

class BookService:
    def __init__(self):
        self.book_repository = BookRepository()
        # self.loan_repository = LoanRepository()  # if you need to check borrowing status

    def add_book(self, title, author, genre, publication_date):
        """
        Adds a new book to the library.
        Business logic: possibly check duplicates, handle mandatory fields, etc.
        """
        # Example: check if the book already exists, etc.
        book = self.book_repository.find_by_title_and_author(title, author)
        if book:
            raise ValueError(f"Book '{title}' by '{author}' already exists in the library.")

        new_book = self.book_repository.create(title, author, genre, publication_date)
        return new_book

    def update_book(self, book_id, **kwargs):
        """
        Updates an existing book's attributes (title, author, etc.).
        """
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        # Update fields
        updated_book = self.book_repository.update(book, **kwargs)
        return updated_book

    def delete_book(self, book_id):
        """
        Deletes a book by its ID (if not currently borrowed, if that rule applies).
        """
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Optional: check if book is currently borrowed
        # if self.loan_repository.is_book_borrowed(book_id):
        #     raise ValueError("Cannot delete a borrowed book.")

        self.book_repository.delete(book)
        return True

    def get_all_books(self):
        """
        Returns a list of all books in the library.
        """
        return self.book_repository.find_all()

    def get_emprunted_books(self):
        """
        Returns a list of currently borrowed books (inventory check).
        """
        return self.book_repository.find_borrowed_books()
