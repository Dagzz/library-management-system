from PyQt5.QtWidgets import QApplication
import sys

from src.app_container import AppContainer

def main():
    app = QApplication(sys.argv)

    container = AppContainer()
    
    container.show_initial_ui()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
