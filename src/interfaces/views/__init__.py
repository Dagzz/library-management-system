"""
Initialization module for views.

This module aggregates all the views, including admin views, user views, 
and general views, to simplify imports and improve project organization. 
"""

from .login_view import LoginView
from .main_window import MainWindow
from .admin_views import (
    AdminMainView,
    BookManagementView,
    UserManagementView
)
from .user_views import (
    BookReservationView,
    BorrowedBookView,
    SearchBookView,
    UserMainView
)

__all__ = [
    "LoginView",
    "MainWindow",
    "AdminMainView",
    "BookManagementView",
    "UserManagementView",
    "BookReservationView",
    "BorrowedBookView",
    "SearchBookView",
    "UserMainView",
]
