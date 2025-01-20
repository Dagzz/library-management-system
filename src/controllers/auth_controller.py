from PyQt5.QtWidgets import QMessageBox
from src.services.authentication_service import AuthenticationService

class AuthController:
    def __init__(self, auth_service, login_view):
        self.login_view = login_view
        self.auth_service = auth_service
        self.login_view.show()
        # Connect the login button
        self.login_view.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        login, password = self.login_view.get_credentials()

        # Call the service to validate credentials
        user = self.auth_service.validate_credentials(login, password)
        if user:
            self.login_view.accept()  # Close the dialog
            # self.main_window.show()   # Show the main app
        else:
            QMessageBox.warning(self.login_view, "Login Failed", "Invalid credentials.")
