import sys
from PyQt6.QtWidgets import QApplication
from src.core.config.logging_loader import logger
from src.core.config.app_container import AppContainer
from src.interfaces.controllers.main_controller import MainController

def main():
    
    logger.info("Starting Library management System.") 
    app = QApplication(sys.argv)
    
    logger.info("Starting Application Container")
    try:
        app_container = AppContainer()    
    except Exception as e:
        logger.error(f"Failed to initialize application container: {e}")
        sys.exit(1)
    
    logger.info("Starting the Main Controller")
    try:
        main_controller = MainController(app_container)
    except Exception as e:
        logger.error(f"Failed to initialize the main controller: {e}")
        sys.exit(1)
    
    main_controller.start()
    
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()
