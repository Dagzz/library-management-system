"""
Initialization file for the repositories package.

This package provides:
- Repository classes for interacting with database models.
- Encapsulation of database operations related to each model.

Repositories:
- CityRepository
- AddressRepository
- UserRepository
- RoleRepository
- LanguageRepository
- CollectionRepository
- AuthorRepository
- GenreRepository
- BookRepository
- LoanRepository
- ReservationRepository
- ModificationRepository
- AuthenticationRepository
"""

from .city_repository import CityRepository
from .address_repository import AddressRepository
from .user_repository import UserRepository
from .role_repository import RoleRepository
from .language_repository import LanguageRepository
from .collection_repository import CollectionRepository
from .author_repository import AuthorRepository
from .genre_repository import GenreRepository
from .book_repository import BookRepository
from .loan_repository import LoanRepository
from .reservation_repository import ReservationRepository
from .modification_repository import ModificationRepository
from .authentication_repository import AuthenticationRepository

__all__ = [
    "CityRepository",
    "AddressRepository",
    "UserRepository",
    "RoleRepository",
    "LanguageRepository",
    "CollectionRepository",
    "AuthorRepository",
    "GenreRepository",
    "BookRepository",
    "LoanRepository",
    "ReservationRepository",
    "ModificationRepository",
    "AuthenticationRepository", 
]
