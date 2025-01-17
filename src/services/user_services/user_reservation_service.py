from datetime import datetime
from src.repositories.reservation_repository import ReservationRepository
from src.repositories.user_repository import UserRepository
from src.repositories.book_repository import BookRepository
from src.repositories.loan_repository import LoanRepository

class UserReservationService:
    def __init__(self):
        self.reservation_repository = ReservationRepository()
        self.user_repository = UserRepository()
        self.book_repository = BookRepository()
        self.loan_repository = LoanRepository()

    def create_reservation(self, user_id, book_id):
        """
        Create a reservation for a user if:
          - User exists and is active
          - User does not already have an active reservation
          - The book is not already reserved by another user
          - The book is currently borrowed or unavailable, so reservation makes sense
        """
        user = self.user_repository.find_by_id(user_id)
        book = self.book_repository.find_by_id(book_id)

        if not user or not user.is_active:
            raise ValueError("User is not active or does not exist.")

        # Rule: a user can only have 1 active reservation at a time
        if self.reservation_repository.count_active_reservations_for_user(user_id) >= 1:
            raise ValueError("User already has an active reservation.")

        # Check if the book is already reserved
        if self.reservation_repository.is_book_reserved(book_id):
            raise ValueError("Book is already reserved by another user.")

        # Optionally, check if the book is currently borrowed
        # If it’s not borrowed, user might directly borrow it instead
        if not self.loan_repository.is_book_borrowed(book_id):
            raise ValueError("This book is not currently borrowed. Please borrow it directly.")

        # If all checks pass, create the reservation
        new_reservation = self.reservation_repository.create_reservation(user, book)
        return new_reservation

    def cancel_reservation(self, reservation_id):
        """
        Cancel a reservation (e.g., user changed their mind or admin override).
        """
        reservation = self.reservation_repository.find_by_id(reservation_id)
        if not reservation or reservation.canceled_date is not None:
            raise ValueError("Invalid or already-canceled reservation.")

        self.reservation_repository.cancel_reservation(reservation)
        return True

    def get_active_reservations_for_user(self, user_id):
        """
        Return a list of active reservations for a given user.
        """
        return self.reservation_repository.find_active_by_user(user_id)

    def get_all_active_reservations(self):
        """
        Return all active reservations (e.g., for admin to review).
        """
        return self.reservation_repository.find_all_active()

    def mark_book_as_available_for_next_in_line(self, book_id):
        """
        If a book just got returned, notify or transfer it to the next person 
        in the reservation queue (if you have a queue system).
        """
        # Here, you'd implement logic for multiple reservations in a queue.
        # If you only allow one reservation per book at a time, 
        # fetch the single reservation and handle notification.
        reservation = self.reservation_repository.find_active_reservation_for_book(book_id)
        if reservation:
            # e.g., send a notification or do any logic to finalize the reservation
            # Possibly set a 'ready_to_pickup_date' or something similar
            reservation.ready_to_pickup_date = datetime.now()
            self.reservation_repository.update_reservation(reservation)

    def enforce_no_extension_if_reserved(self, book_id):
        """
        Called by LoanService's 'extend_loan' to check if the book is reserved.
        If there is an active reservation on this book, disallow extension.
        """
        if self.reservation_repository.is_book_reserved(book_id):
            raise ValueError("Cannot extend the loan because this book is reserved.")
        return True
