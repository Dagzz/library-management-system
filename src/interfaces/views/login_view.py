from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt 
import src.resources.settings as st

class LoginView(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle("Warcraft Library")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon(st.ICON_PATH))
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

    def load_styles(self):
        # Load the styles from the external stylesheet
        with open(st.QSS_FILE, "r") as file:
            self.setStyleSheet(file.read())

    def center_window(self):
        screen_geometry = self.screen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def get_credentials(self):
        return self.login_input.text(), self.password_input.text()
