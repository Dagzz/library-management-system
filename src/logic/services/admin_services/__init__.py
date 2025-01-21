"""
Initialization module for admin services.

This module consolidates all the admin-specific service classes, which 
contain business logic related to administrative functionalities, such 
as managing books, loans, and users.
"""

from .admin_book_service import AdminBookService
from .admin_loan_service import AdminLoanService
from .admin_user_service import AdminUserService

__all__ = [
    "AdminBookService",
    "AdminLoanService",
    "AdminUserService",
]
