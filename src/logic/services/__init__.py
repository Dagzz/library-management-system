"""
Initialization module for services.

This module consolidates all service classes, which contain the business logic 
for the application, divided into admin-specific, user-specific, and general services.
"""

# General Services
from .authentication_service import AuthenticationService

# Admin Services
from .admin_services import (
    AdminBookService,
    AdminLoanService,
    AdminUserService,
)

# User Services
from .user_services import (
    UserBookService,
    UserLoanService,
    UserReservationService,
)

__all__ = [
    # General Services
    "AuthenticationService",
    
    # Admin Services
    "AdminBookService",
    "AdminLoanService",
    "AdminUserService",
    
    # User Services
    "UserBookService",
    "UserLoanService",
    "UserReservationService",
]
