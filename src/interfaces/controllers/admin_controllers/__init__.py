"""
Admin Controllers

This package contains controllers used to manage admin-specific features
such as managing books, loans, and user accounts.

Available Controllers:
- AdminBookController: Handles admin operations related to books.
- AdminLoanController: Manages admin-specific loan-related functionalities.
- AdminUserController: Admin functionality for managing users.

Usage:
- Import the required controller:
    from src.interfaces.controllers.admin_controllers import AdminBookController
"""

from .admin_book_controller import AdminBookController
from .admin_loan_controller import AdminLoanController
from .admin_user_controller import AdminUserController

__all__ = [
    "AdminBookController",
    "AdminLoanController",
    "AdminUserController",
]
