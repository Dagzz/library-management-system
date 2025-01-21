"""
ReservationRepository

Handles database operations related to the `Reservation` model.

Responsibilities:
- Managing reservation records, including creating, updating, or deleting reservations.
- Fetching reservations by ID, user, or book.
- Checking the reservation status of specific books.
- Querying confirmed and pending reservations.

Usage:
- Initialize with a session factory:
    repo = ReservationRepository(get_session)
- Use the provided methods to perform CRUD operations and retrieve reservation data.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from src.core.models import Reservation 

class ReservationRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        """
        Fetch a reservation by its ID.
        """
        return self.session.query(Reservation).filter(Reservation.id_reservation == reservation_id).one_or_none()

    def get_reservations_by_user(self, user_id: int) -> List[Reservation]:
        """
        Fetch all reservations for a specific user.
        """
        return self.session.query(Reservation).filter(Reservation.id_user == user_id).all()

    def get_reservations_by_book(self, book_id: int) -> List[Reservation]:
        """
        Fetch all reservations for a specific book.
        """
        return self.session.query(Reservation).filter(Reservation.id_book == book_id).all()

    def get_reservations_by_status(self, is_confirmed: bool) -> List[Reservation]:
        """
        Fetch all reservations by their confirmation status.
        """
        return self.session.query(Reservation).filter(Reservation.is_confirmed == is_confirmed).all()

    def add_reservation(self, reservation: Reservation) -> Reservation:
        """
        Add a new reservation.
        """
        self.session.add(reservation)
        self.session.commit()
        return reservation

    def update_reservation(self, reservation: Reservation) -> Reservation:
        """
        Update an existing reservation.
        """
        self.session.merge(reservation)
        self.session.commit()
        return reservation

    def delete_reservation(self, reservation_id: int) -> bool:
        """
        Delete a reservation by its ID.
        """
        reservation = self.get_reservation_by_id(reservation_id)
        if reservation:
            self.session.delete(reservation)
            self.session.commit()
            return True
        return False

    def get_reservations_by_user_and_status(self, user_id: int, is_confirmed: bool) -> List[Reservation]:
        """
        Fetch reservations for a user with a specific confirmation status.
        """
        return (
            self.session.query(Reservation)
            .filter(Reservation.id_user == user_id, Reservation.is_confirmed == is_confirmed)
            .all()
        )

    def get_reservations_for_book_and_status(self, book_id: int, is_confirmed: bool) -> List[Reservation]:
        """
        Fetch reservations for a book with a specific confirmation status.
        """
        return (
            self.session.query(Reservation)
            .filter(Reservation.id_book == book_id, Reservation.is_confirmed == is_confirmed)
            .all()
        )