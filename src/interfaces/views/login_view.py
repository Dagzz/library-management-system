"""
LoginView

This class represents the login dialog for the Warcraft Library application.

Responsibilities:
- Provides the user interface for user authentication.
- Collects user credentials (username and password) and allows users to attempt login.
- Loads and applies styles from an external stylesheet for a consistent UI design.

Key Components:
- Username Input: A text field for the user to input their username.
- Password Input: A secure text field for entering the password, with input masked for security.
- Login Button: A button to trigger the login process.

Key Methods:
- `__init__`: Initializes the dialog and sets up the user interface.
- `init_ui`: Constructs the UI elements, layouts, and styling for the dialog.
- `load_styles`: Loads and applies styles from an external `.qss` stylesheet.
- `center_window`: Centers the login dialog on the user's screen.
- `get_credentials`: Returns the username and password entered by the user as a tuple.

Usage:
- Instantiated and displayed by the `AuthController` for user authentication.
- Interacts with the authentication service to validate user credentials.
"""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
import src.core.config.assets_paths as ap
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
import src.core.config.assets_paths as ap
from src.interfaces.views.custom_error import CustomErrorDialog

class LoginView(QDialog):
    def __init__(self):
        """
        Initializes the LoginView dialog.
        
        - Sets up the UI components.
        - Applies styles using an external stylesheet.
        """
        super().__init__()
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        """
        Constructs and arranges the UI elements for the login dialog.
        
        - Sets the dialog's title, size, and icon.
        - Creates input fields for username and password.
        - Adds a login button and organizes all elements in layouts.
        """
        self.setWindowTitle("Warcraft Library")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon(ap.AUTH_ICON))
        self.center_window()
        self.setObjectName("loginWindow")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Spacer to push content to the bottom
        top_spacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        
        # Username Input
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Enter your username")

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Enter your password")

        # Button
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.login_button = QPushButton("Login")

        button_layout.addWidget(self.login_button)

        main_layout.addItem(top_spacer)  
        main_layout.addWidget(self.login_input)
        main_layout.addWidget(self.password_input)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def load_styles(self) -> None:
        """
        Loads and applies styles to the dialog from an external `.qss` stylesheet.
        
        - Ensures consistent theming across the application's UI.
        - Reads the stylesheet file specified in `ap.QSS_FILE`.
        """
        with open(ap.QSS_FILE, "r") as file:
            self.setStyleSheet(file.read())

    def center_window(self) -> None:
        """
        Centers the dialog on the user's screen.
        
        - Calculates the center of the screen and positions the window accordingly.
        """
        screen_geometry = self.screen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def get_credentials(self) -> tuple[str, str]:
        """
        Retrieves the username and password entered by the user.

        Returns:
            tuple[str, str]: A tuple containing the username and password.
        """
        return self.login_input.text(), self.password_input.text()
    
    def show_credentials_error_message(self) -> None:
        """
        Displays a custom error message box with a custom icon for failed login attempts.
        """
        error_dialog = CustomErrorDialog(
            title="Authentication Failed",
            message="Invalid credentials.\nPlease try again.",
            icon_path=ap.AUTH_ERROR,
            dialog_icon_path= ap.AUTH_ERROR_ICON
        )
        error_dialog.exec()
        
    def show_connection_error_message(self) -> None:
        """
        Displays a custom error message box with a custom icon for failed login attempts.
        """
        error_dialog = CustomErrorDialog(
            title="Authentication Failed",
            message="Oops! There seems to be an issue on our end. Please wait a moment or contact support.",
            icon_path=ap.AUTH_ERROR,
            dialog_icon_path= ap.AUTH_ERROR_ICON
        )
        error_dialog.exec()
        
            
        

