import sys
from PyQt6.QtWidgets import QApplication
from src.controllers.main_controller import MainController

def main():
    
    app = QApplication(sys.argv)
    
    controller = MainController()
    
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()
