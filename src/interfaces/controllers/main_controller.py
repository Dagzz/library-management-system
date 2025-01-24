import sys
from src.core.config.logging_loader import logger
from src.core.session_manager import AppSession

class MainController:
    """
    MainController

    This controller serves as the central orchestrator for the application's flow.

    Responsibilities:
    - Manages the application's lifecycle, starting from authentication to the main window.
    - Coordinates between different controllers and views initialized in the AppContainer.
    - Provides methods to display the main window after successful authentication.

    Key Methods:
    - __init__: Initializes the controller with the application's dependency container (AppContainer).
    - start: Starts the application by activating the authentication controller.
    - show_main_window: Displays the main application window.

    Dependencies:
    - AppContainer: Provides access to all controllers, views, and services required by the application.

    Usage:
    - Instantiated with the AppContainer to centralize and coordinate app functionality.
    - Called by main.py to bootstrap and manage the application flow.
    """
    def __init__(self, app_container) -> None:
        """
        :param app_container: The central container providing controllers, views, and services.
        """
        self.app_container = app_container

    def start(self) -> None:
        """
        Starts the application workflow by initiating the authentication flow.
        """
        logger.info("Starting the application workflow.")
        self.auth_controller = self.app_container.auth_controller
        # Set up callback for success
        self.auth_controller.on_login_success = self.on_auth_success
        self.auth_controller.start_auth_flow()

    def on_auth_success(self):
        session = AppSession()
        print(session)

    def show_role_choice_view(self, user):
        """
        Displays a view/dialog that allows the user to choose
        whether to proceed as an admin or as a regular user.
        """
        chosen_role = self.app_container.role_choice_view.get_user_choice()
        if chosen_role == "admin":
            self.show_admin_main_view(user)
        else:
            self.show_user_main_view(user)


    def show_admin_main_view(self, user):
        """
        Shows the main admin view (e.g., admin dashboard).
        """
        self.app_container.admin_main_view.show()


    def show_user_main_view(self, user):
        """
        Shows the main regular user view.
        """
        self.app_container.user_main_view.show()

