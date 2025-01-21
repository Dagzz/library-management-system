"""
Initialization module for admin views.

This module aggregates all the admin view classes to simplify imports
and improve code organization. Admin views are responsible for 
rendering the UI components related to admin functionalities.
"""

from .admin_main_view import AdminMainView
from .book_management_view import BookManagementView
from .user_management_view import UserManagementView

__all__ = [
    "AdminMainView",
    "BookManagementView",
    "UserManagementView",
]
