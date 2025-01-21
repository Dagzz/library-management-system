from datetime import datetime, timedelta
from src.infra.repositories.loan_repository import LoanRepository
from src.infra.repositories.user_repository import UserRepository
from src.infra.repositories.book_repository import BookRepository

class UserLoanService:
    def __init__(self):
        self.loan_repository = LoanRepository()
        self.user_repository = UserRepository()
        self.book_repository = BookRepository()

    def borrow_book(self, user_id, book_id):
        """
        User borrows a book if user is active, has fewer than 3 borrowed books, 
        and book is available (not borrowed or reserved).
        """
        user = self.user_repository.find_by_id(user_id)
        book = self.book_repository.find_by_id(book_id)

        if not user or not user.is_active:
            raise ValueError("User is not active or does not exist.")
        if self.loan_repository.count_loans_for_user(user_id) >= 3:
            raise ValueError("Cannot borrow more than 3 books at a time.")

        # Check if book is already borrowed
        if self.loan_repository.is_book_borrowed(book_id):
            raise ValueError("Book is already borrowed.")

        # Additional reservation check if needed

        due_date = datetime.now() + timedelta(days=21)
        new_loan = self.loan_repository.create_loan(user, book, due_date)
        return new_loan

    def return_book(self, user_id, book_id):
        """
        User returns a borrowed book; handle overdue logic if needed.
        """
        loan = self.loan_repository.find_active_loan(user_id, book_id)
        if not loan:
            raise ValueError("No active loan found for this user/book.")

        self.loan_repository.close_loan(loan)
        return True

    def extend_loan(self, loan_id):
        """
        Extend a loan by 7 days if no reservation on the book.
        """
        loan = self.loan_repository.find_by_id(loan_id)
        if not loan or loan.returned_date is not None:
            raise ValueError("Invalid or closed loan.")

        # Check reservation or other constraints
        if self.loan_repository.is_book_reserved(loan.book_id):
            raise ValueError("Cannot extend because the book is reserved.")

        # Extend due_date by 7 days
        loan.due_date += timedelta(days=7)
        self.loan_repository.update(loan)
        return loan

    def get_overdue_loans(self):
        """
        Return a list of all overdue loans for admin to handle.
        """
        return self.loan_repository.find_overdue_loans()
