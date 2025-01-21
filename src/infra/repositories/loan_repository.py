"""
LoanRepository

Handles database operations related to the `Loan` model.

Responsibilities:
- Managing loan-related data, including adding, updating, or deleting loan records.
- Fetching loan records by ID, user, or book.
- Querying active loans, overdue loans, or loan history for specific users or books.

Usage:
- Initialize with a session factory:
    repo = LoanRepository(get_session)
- Use the provided methods to perform CRUD operations and queries on the `Loan` table.
"""

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import List, Optional
from src.core.models import Loan, Reservation

class LoanRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_loan_by_id(self, loan_id: int) -> Optional[Loan]:
        """
        Fetch a loan by its ID.
        """
        return self.session.query(Loan).filter(Loan.id_loan == loan_id).one_or_none()

    def get_loans_by_user(self, user_id: int) -> List[Loan]:
        """
        Fetch all loans for a specific user.
        """
        return self.session.query(Loan).filter(Loan.id_user == user_id).all()

    def get_loans_by_book(self, book_id: int) -> List[Loan]:
        """
        Fetch all loans for a specific book.
        """
        return self.session.query(Loan).filter(Loan.id_book == book_id).all()

    def get_active_loans(self) -> List[Loan]:
        """
        Fetch all active loans (loans with no return date yet).
        """
        return self.session.query(Loan).filter(Loan.return_date.is_(None)).all()

    def get_overdue_loans(self) -> List[Loan]:
        """
        Fetch all overdue loans (loans where the return date has passed).
        """
        return (
            self.session.query(Loan)
            .filter(Loan.return_date.isnot(None), Loan.return_date < func.now())
            .all()
        )

    def get_loans_with_reservations(self) -> List[Loan]:
        """
        Fetch all loans where the books are reserved.
        """
        return (
            self.session.query(Loan)
            .join(Reservation, Loan.id_book == Reservation.id_book)
            .filter(Reservation.is_confirmed == True)
            .all()
        )

    def add_loan(self, loan: Loan) -> Loan:
        """
        Add a new loan to the database.
        """
        self.session.add(loan)
        self.session.commit()
        return loan

    def update_loan(self, loan: Loan) -> Loan:
        """
        Update an existing loan in the database.
        """
        self.session.merge(loan)
        self.session.commit()
        return loan

    def delete_loan(self, loan_id: int) -> bool:
        """
        Delete a loan by its ID.
        """
        loan = self.get_loan_by_id(loan_id)
        if loan:
            self.session.delete(loan)
            self.session.commit()
            return True
        return False

    def get_loans_by_user_and_status(self, user_id: int, is_active: bool) -> List[Loan]:
        """
        Fetch loans for a user filtered by active status.
        """
        if is_active:
            return self.session.query(Loan).filter(Loan.id_user == user_id, Loan.return_date.is_(None)).all()
        else:
            return self.session.query(Loan).filter(Loan.id_user == user_id, Loan.return_date.isnot(None)).all()
