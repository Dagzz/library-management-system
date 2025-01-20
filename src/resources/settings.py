import os

# Base path for assets
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '...'))

# Fonts Path
# FONT_PATH_1 = os.path.join(BASE_DIR, 'minesweeper', 'src', 'assets', 'fonts', 'Creepster', 'Creepster-Regular.ttf')

# Images paths
ICON_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'app_icon.png')
AUTH_BG = os.path.join(BASE_DIR, 'assets', 'images', 'auth.png')

#QSS File
QSS_FILE = os.path.join(BASE_DIR, 'styles', 'styles.qss')
