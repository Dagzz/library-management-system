from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class CustomErrorDialog(QDialog):
    def __init__(self, title: str, message: str, icon_path: str, dialog_icon_path: str):
        """
        Initializes a custom error dialog with a custom icon.

        Args:
            title (str): The title of the dialog.
            message (str): The error message to display.
            icon_path (str): The path to the custom icon to display inside the dialog.
            dialog_icon_path (str): The path to the icon for the dialog window.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon(dialog_icon_path))
        self.init_ui(message, icon_path)

    def init_ui(self, message: str, icon_path: str) -> None:
        """
        Creates the UI for the dialog, including a custom icon.

        Args:
            message (str): The error message to display.
            icon_path (str): The path to the custom icon to display inside the dialog.
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 20, 20)
        layout.setSpacing(10)

        # Icon and message layout
        icon_label = QLabel()
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(170, 170, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            icon_label.setText("Icon not found")  
        icon_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        icon_message_layout = QHBoxLayout()
        icon_message_layout.addWidget(icon_label)
        icon_message_layout.addWidget(message_label)

        # Spacer
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # OK Button
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.close)
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        button_layout.addWidget(ok_button)

        # Add to main layout
        layout.addLayout(icon_message_layout)
        layout.addSpacerItem(spacer)
        layout.addLayout(button_layout)

        self.setLayout(layout)
