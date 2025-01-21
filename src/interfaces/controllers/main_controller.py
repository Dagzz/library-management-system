"""
MainController

This controller serves as the central orchestrator for the application's flow.

Responsibilities:
- Manages the application's lifecycle, starting from authentication to the main window.
- Coordinates between different controllers and views initialized in the AppContainer.
- Provides methods to display the main window after successful authentication.

Key Methods:
- `__init__`: Initializes the controller with the application's dependency container (`AppContainer`).
- `start`: Starts the application by activating the authentication controller.
- `show_main_window`: Displays the main application window.

Dependencies:
- AppContainer: Provides access to all controllers, views, and services required by the application.

Usage:
- Instantiated with the AppContainer to centralize and coordinate app functionality.
- Called by `main.py` to bootstrap and manage the application flow.
"""
import sys
# from src.core.config.app_container import AppContainer
from src.core.config.logging_loader import logger

class MainController:
    def __init__(self, app_container):
        self.app_container = app_container

    def start(self):
        logger.info("Starting the authentication controller.")
        try:
            auth_controller = self.app_container.auth_controller
        except Exception as e:
            logger.error(f"Failed to initialize the authentication controller: {e}.")
            sys.exit(1)
       

    def show_main_window(self):
        main_window = self.app_container.main_window
        main_window.show()
