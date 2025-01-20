# Session factory
from src.database.database_connection import get_session

# Repositories
from src.repositories.city_repository import CityRepository
from src.repositories.address_repository import AddressRepository
from src.repositories.user_repository import UserRepository
from src.repositories.role_repository import RoleRepository
from src.repositories.language_repository import LanguageRepository
from src.repositories.collection_repository import CollectionRepository
from src.repositories.author_repository import AuthorRepository
from src.repositories.genre_repository import GenreRepository
from src.repositories.book_repository import BookRepository
from src.repositories.loan_repository import LoanRepository
from src.repositories.reservation_repository import ReservationRepository
from src.repositories.modification_repository import ModificationRepository

# Services
from src.services.authentication_service import AuthenticationService

## User Services
from src.services.user_services.user_book_service import UserBookService
from src.services.user_services.user_loan_service import UserLoanService
from src.services.user_services.user_reservation_service import UserReservationService

## Admin Services
from src.services.admin_services.admin_book_service import AdminBookService
from src.services.admin_services.admin_loan_service import AdminLoanService
from src.services.admin_services.admin_user_service import AdminUserService

# Controllers
from src.controllers.auth_controller import AuthController

## Users Controllers
from src.controllers.user_controllers.user_book_controller import UserBookController
from src.controllers.user_controllers.user_reservation_controller import UserReservationController
from src.controllers.user_controllers.user_loan_controller import UserLoanController

## Admin Controllers
from src.controllers.admin_controllers.admin_book_controller import AdminBookController
from src.controllers.admin_controllers.admin_user_controller import AdminUserController
from src.controllers.admin_controllers.admin_loan_controller import AdminLoanController

# Views
# from src.views.book_view import BookView
# from src.views.user_view import UserView
# from src.views.loan_view import LoanView
from src.views.login_view import LoginView
from src.views.main_window import MainWindow 

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
        self.book_repo = BookRepository(get_session)
        self.user_repo = UserRepository(get_session)
        self.loan_repo = LoanRepository(get_session)
        
        # Create Services
        self.auth_service = AuthenticationService(self.book_repo)

        # Create Views
        self.login_view = LoginView()
        self.main_window = MainWindow()

        # Create Controllers
        self.auth_controller = AuthController(self.auth_service, self.login_view)
        
        # Possibly pass main_window into some "MainController" if you have one

    def show_initial_ui(self):
        """
        Decide which UI to show first (login window, main window, etc.).
        """
        self.login_view.show()
        # Once the user is authenticated, the login_controller might show the main_window, etc.
