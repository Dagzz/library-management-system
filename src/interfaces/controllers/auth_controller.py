from PyQt6.QtWidgets import QMessageBox
from src.services.authentication_service import AuthenticationService

class AuthController:
    def __init__(self, auth_service, login_view):
        self.login_view = login_view
        self.auth_service = auth_service
        self.login_view.show()

        self.login_view.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        login, password = self.login_view.get_credentials()

        # Call the service to validate credentials
        try:
            auth = self.auth_service.authenticate_user(login, password)
            self.login_view.accept()
            print("Authentication successful")
            # self.main_window.show()
        except ValueError as e:
            QMessageBox.warning(self.login_view, "Login Failed", "Invalid credentials.")