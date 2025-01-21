"""
AuthController

This controller manages the authentication workflow in the application.

Responsibilities:
- Manages user interactions in the login view.
- Handles user login by validating credentials using the AuthenticationService.
- Displays appropriate messages for successful or failed login attempts.

Key Methods:
- `__init__`: Initializes the controller, sets up the view, and binds events.
- `handle_login`: Handles the login logic, including credential validation 
  and feedback to the user.

Dependencies:
- AuthenticationService: Validates user credentials.
- LoginView: Provides the user interface for login.

Usage:
- Instantiated with the AuthenticationService and LoginView.
- Automatically shows the login view on initialization.
"""

from src.core.config.logging_loader import logger

class AuthController:
    def __init__(self, auth_service, login_view):
        self.login_view = login_view
        self.auth_service = auth_service
        self.login_view.show()

        # Connect Button(s)
        self.login_view.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        
        logger.info("Initiating the user authentication process.")
        login, password = self.login_view.get_credentials()
            
        try:
            self.auth_service.authenticate_user(login, password)
            self.login_view.accept()
            logger.info("User authentication successful for username: %s.", login)
            # self.main_window.show()
        except ValueError as e:
            logger.error("Authentication failed for username: %s. Reason: %s", login, str(e))
            self.login_view.show_error_message()
