import sys
from PyQt6.QtWidgets import QApplication
from src.app_container import AppContainer
from src.controllers.main_controller import MainController
from src.resources.config.logging_loader import setup_logger

logger = setup_logger()

def main():
    
    logger.info("Starting Library management System.")
    
    app = QApplication(sys.argv)

    app_container = AppContainer()
    
    main_controller = MainController(app_container)
    
    main_controller.start()
    
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()
