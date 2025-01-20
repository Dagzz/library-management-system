from PyQt6.QtWidgets import QApplication
import sys
from src.app_container import AppContainer
from src.controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)

    app_container = AppContainer()
    
    main_controller = MainController(app_container)
    
    main_controller.start()
    
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()
