import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt



class AuthenticationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        container = QWidget()
        main_layout = QVBoxLayout(container) 
        
        main_layout.addStretch()
        form_layout = QVBoxLayout()
        self.setWindowIcon(QIcon("library-management-system/src/resources/images/icon.png"))

        # Titre
        self.title_label = QLabel("Authentication")
        self.title_label.setObjectName("titleLabel")
        form_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Champ de login
        self.login_label = QLabel("Login:")
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Enter your login")
        form_layout.addWidget(self.login_label)
        form_layout.addWidget(self.login_input)

        # Champ de mot de passe
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Enter your password")
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)

        # Bouton de validation
        self.submit_button = QPushButton("Login")
        self.submit_button.clicked.connect(self.handle_login)
        form_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Ajouter le formulaire centré au layout principal
        main_layout.addLayout(form_layout)

        # Stretch pour centrer verticalement
        main_layout.addStretch()

        self.setCentralWidget(container)

    def handle_login(self):
        # Récupération des données saisies
        login = self.login_input.text()
        password = self.password_input.text()

        # Affichage en console (remplacer par une logique réelle)
        print(f"Login: {login}")
        print(f"Password: {password}")

        # Exemple de logique de validation
        if login == "admin" and password == "password":
            print("Login successful!")
        else:
            print("Invalid credentials!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthenticationWindow()
    sys.exit(app.exec())