"""
Controllers

This package serves as the entry point for all controllers in the application.
It contains both general-purpose controllers and sub-packages for specific user roles 
(admin and user).

Available Controllers:
- AuthController: Manages authentication processes such as login and logout.
- MainController: Handles the main application workflow and navigation.

Sub-packages:
- admin_controllers: Contains controllers specific to admin functionality.
- user_controllers: Contains controllers specific to user functionality.

Usage:
- Import general controllers:
    from src.interfaces.controllers import AuthController
- Import role-specific controllers from sub-packages:
    from src.interfaces.controllers.admin_controllers import AdminBookController
    from src.interfaces.controllers.user_controllers import UserBookController
"""

from .auth_controller import AuthController
from .main_controller import MainController

__all__ = [
    "AuthController",
    "MainController",
]
