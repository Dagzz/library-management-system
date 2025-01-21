from src.app_container import AppContainer

class MainController:
    def __init__(self, app_container : AppContainer):
        self.app_container = app_container

    def start(self):
        auth_controller = self.app_container.auth_controller

    def show_main_window(self):
        main_window = self.app_container.main_window
        main_window.show()
