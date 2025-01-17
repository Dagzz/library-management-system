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
from src.services.auth_service import AuthService

## User Services
from src.services.user_service import UserService
from src.services.loan_service import LoanService
from src.services.reservation_service import ReservationService
from src.services.auth_service import AuthService  # userService for now, to implement after

## Admin Services

# Controllers
from src.controllers.login_controller import LoginController

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
    - Database session
    - Repositories
    - Services
    - Controllers
    - Views
    """
    def __init__(self):
        
        # Session-per-transaction model
        # Pass the session factory (get_session) instead of a single session
        # Manage the session lifecycle at the repository level
        
        # 2. Create Repositories
        self.book_repo = BookRepository(get_session)
        self.user_repo = UserRepository(get_session)
        self.loan_repo = LoanRepository(get_session)
        
        # 3. Create Services
        self.book_service = BookService(self.book_repo)
        self.user_service = UserService(self.user_repo)
        self.loan_service = LoanService(self.loan_repo)

        # 4. Create Views
        self.login_view = LoginView()
        self.main_window = MainWindow()  # optional, if you have a main window

        # 5. Create Controllers (inject required services + views)
        self.book_controller = BookController(self.book_service, self.book_view)
        self.user_controller = UserController(self.user_service, self.user_view)
        self.loan_controller = LoanController(self.loan_service, self.loan_view)
        self.login_controller = LoginController(self.user_service, self.login_view)
        # Possibly pass main_window into some "MainController" if you have one

    def show_initial_ui(self):
        """
        Decide which UI to show first (login window, main window, etc.).
        """
        # Example: show the login view first
        self.login_view.show()
        # Once the user is authenticated, the login_controller might show the main_window, etc.
