"""
Initialization module for styles.

This module provides access to style-related resources, including stylesheets
used to define the application's visual appearance.

Exports:
- The path to the primary stylesheet (`styles.qss`).
"""

import os

# Path to the styles.qss file
STYLESHEET_PATH = os.path.join(os.path.dirname(__file__), "styles.qss")

__all__ = ["STYLESHEET_PATH"]
