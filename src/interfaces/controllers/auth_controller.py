from src.core.config.logging_loader import logger
from src.core.custom_exceptions import DatabaseUpdateError

class AuthController:
    """
    AuthController

    This controller manages the authentication workflow in the application.

    Responsibilities:
    - Manages user interactions in the login view.
    - Handles user login by validating credentials using the AuthenticationService.
    - Displays appropriate messages for successful or failed login attempts.

    Key Methods:
    - __init__: Initializes the controller, sets up the view, and binds events.
    - start_auth_flow: Called by MainController to show the login view and wait for user action.
    - handle_login: Handles the actual login logic, including credential validation and feedback.

    Dependencies:
    - AuthenticationService: Validates user credentials.
    - LoginView: Provides the user interface for login.

    Usage:
    - Instantiated with the AuthenticationService and LoginView.
    - The on_login_success and on_login_failure callbacks are assigned by MainController.
    """

    def __init__(self, auth_service, login_view):
        """
        :param auth_service: A service providing user credential validation.
        :param login_view: The view that handles user login UI.
        """
        self.auth_service = auth_service
        self.login_view = login_view

        # Callbacks (set by MainController)
        self.on_login_success = None  # Expected signature: on_login_success()

    def start_auth_flow(self):
        """
        Displays the login view and connects the login button to handle_login.
        """
        self.login_view.show()
        self.login_view.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        """
        Retrieves user credentials from the login view, attempts authentication, 
        and invokes the appropriate callback on success.
        """
        logger.info("Initiating the user authentication process.")
        login, password = self.login_view.get_credentials()

        try:
            # The authenticate_user method should return a user id
            id_user = self.auth_service.authenticate_user(login, password)
            logger.info("Updating the last connection date.")
            
            try:
                self.auth_service.update_user_last_connection_date(id_user)
            except DatabaseUpdateError as e:
                # Minor error, we handle it here
                logger.warning(
                    "Failed to update last connection date for user '%s'. Proceeding with login. Reason: %s",
                    login,
                    str(e)
                )
            logger.info("Setting user session.")
            self.auth_service.set_user_session(id_user)

            logger.info("User authentication successful for username: %s.", login)
            # Notify MainController of success
            if self.on_login_success:
                self.on_login_success()

            # Close the login view
            self.login_view.accept()

        except ValueError as e:
            logger.error("Authentication failed for username '%s'. Reason: %s", login, str(e))
            # Show error message to the user
            self.login_view.show_credentials_error_message()
        except ConnectionError as e:
            logger.error("Connection issue while authenticating username '%s'. Reason: %s", login, str(e))
            self.login_view.show_connection_error_message()
            
    def update_user_last_connection(self, id_user: int) -> None:
        """
        Update the new connection date time for the user.

        Args:
            id_user (int): The ID of the user.
        """
        try:
            self.auth_service.update_user_last_connection_date(id_user)
            logger.info("Last connection date update successfull for id user: %s.", id_user)
        except ValueError as e:
            logger.error("Error updating last connection date for user ID: %s. Reason: %s", id_user, str(e))
    
    def set_user_session(self, id_user: int) -> None:
        """
        Handles setting the user session and logging the process.

        Args:
            id_user (int): The ID of the user.
        """
        try:
            session_data = self.auth_service.set_user_session(id_user)
            logger.info("User session set successfully for ID: %s. Session data: %s", id_user, session_data)
        except ValueError as e:
            logger.error("Error setting user session for ID: %s. Reason: %s", id_user, str(e))
            raise e