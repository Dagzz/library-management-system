"""
Centralizes file paths for static assets (images, stylesheets, fonts).
This simplifies asset management and avoids hardcoding paths across the project.
"""

import os

# Base path for static assets
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Fonts Paths
# FONT_PATH_1 = os.path.join(BASE_DIR, 'static', 'fonts', 'Creepster-Regular.ttf')

# Icons paths
APP_ICON = os.path.join(BASE_DIR, 'static', 'images', 'icons', 'app_icon.png')
AUTH_ICON = os.path.join(BASE_DIR, 'static', 'images', 'icons', 'auth_icon.png')
AUTH_ERROR_ICON = os.path.join(BASE_DIR, 'static', 'images', 'icons', 'auth_error_icon.png')

# Images paths
AUTH_BG = os.path.join(BASE_DIR, 'static', 'images', 'auth.png')
AUTH_ERROR = os.path.join(BASE_DIR, 'static', 'images', 'auth_error.png')

# QSS File Path
QSS_FILE = os.path.join(BASE_DIR, 'static', 'styles', 'styles.qss')