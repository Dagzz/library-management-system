"""
Defines the application container responsible for managing and wiring
dependencies such as repositories, services, controllers, and views.

Purpose:
- Centralizes the creation and injection of dependencies.
- Simplifies dependency management by reducing tight coupling.
- Serves as the entry point for initializing the application's components.

Structure:
- INFRA: Handles database session and repositories.
- LOGIC: Manages business logic through services.
- INTERFACES: Connects controllers to views for user interaction.

Usage:
- Initialize the container to create all components:
    container = AppContainer()
"""
# INFRA
## Session factory
from src.infra.database.database_connection import get_session

## Repositories
from src.infra.repositories.city_repository import CityRepository
from src.infra.repositories.address_repository import AddressRepository
from src.infra.repositories.user_repository import UserRepository
from src.infra.repositories.role_repository import RoleRepository
from src.infra.repositories.language_repository import LanguageRepository
from src.infra.repositories.collection_repository import CollectionRepository
from src.infra.repositories.author_repository import AuthorRepository
from src.infra.repositories.genre_repository import GenreRepository
from src.infra.repositories.book_repository import BookRepository
from src.infra.repositories.loan_repository import LoanRepository
from src.infra.repositories.reservation_repository import ReservationRepository
from src.infra.repositories.modification_repository import ModificationRepository
from src.infra.repositories.authentication_repository import AuthenticationRepository

# LOGIC
## Services
from src.logic.services.authentication_service import AuthenticationService

### User Services
from src.logic.services.user_services.user_book_service import UserBookService
from src.logic.services.user_services.user_loan_service import UserLoanService
from src.logic.services.user_services.user_reservation_service import UserReservationService

### Admin Services
from src.logic.services.admin_services.admin_book_service import AdminBookService
from src.logic.services.admin_services.admin_loan_service import AdminLoanService
from src.logic.services.admin_services.admin_user_service import AdminUserService

# INTERFACES
## Controllers
from src.interfaces.controllers.auth_controller import AuthController

### Users Controllers
from src.interfaces.controllers.user_controllers.user_book_controller import UserBookController
from src.interfaces.controllers.user_controllers.user_reservation_controller import UserReservationController
from src.interfaces.controllers.user_controllers.user_loan_controller import UserLoanController

### Admin Controllers
from src.interfaces.controllers.admin_controllers.admin_book_controller import AdminBookController
from src.interfaces.controllers.admin_controllers.admin_user_controller import AdminUserController
from src.interfaces.controllers.admin_controllers.admin_loan_controller import AdminLoanController

# INTERFACES
## Views
# from src.views.book_view import BookView
# from src.views.user_view import UserView
# from src.views.loan_view import LoanView
from src.interfaces.views.login_view import LoginView
from src.interfaces.views.main_window import MainWindow 

### Users Views

### Admin Views

class AppContainer:
    """
    Responsible for creating and wiring all dependencies:
    - Session factory
    - Repositories
    - Services
    - Controllers
    - Views
    """
    def __init__(self):
        
        # Session-per-transaction model
        # Pass the session factory (get_session) instead of a single session
        # Manage the session lifecycle at the repository level

        # Create Repositories
        self.auth_repo = AuthenticationRepository(get_session)
        self.role_repo = RoleRepository(get_session)
        self.user_repo = UserRepository(get_session)
        self.book_repo = BookRepository(get_session)
        self.loan_repo = LoanRepository(get_session)
        
        # Create Services
        self.auth_service = AuthenticationService(self.auth_repo, self.user_repo, self.role_repo)

        # Create Views
        self.login_view = LoginView()
        self.main_window = MainWindow()

        # Create Controllers
        self.auth_controller = AuthController(self.auth_service, self.login_view)