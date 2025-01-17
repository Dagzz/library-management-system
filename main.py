from PyQt5.QtWidgets import QApplication
import sys

from src.views.login_view import LoginView
from src.views.main_window import MainWindow 
from src.controllers.login_controller import LoginController

def main():
    app = QApplication(sys.argv)

    # Create the main window, but don't show it yet
    main_window = MainWindow()

    # Create the login view (a QDialog)
    login_view = LoginView()

    # Create the controller that links them
    auth_controller = LoginController(login_view, main_window)

    # Show the login dialog
    # The dialog will only close if credentials are valid (see handle_login logic)
    login_result = login_view.exec_()  

    # If login_result != QDialog.Accepted, the user either failed to log in or closed the dialog
    # Check the controller's logic to see how you handle an unsuccessful login
    if login_result == login_view.Accepted:
        # The user has successfully logged in, and the main window is shown from the controller
        sys.exit(app.exec_())
    else:
        # Login canceled or failed -> exit the application
        sys.exit(0)

if __name__ == "__main__":
    main()
