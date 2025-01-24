"""
Core Package

This package contains the foundational elements of the application:
- Configuration management and utilities.
- Application-wide logging setup.
- Database models shared across the application.

Modules:
- `config`: Contains utilities for configuration loading (`config_loader.py`), 
  logging setup (`logging_loader.py`), and other app-level setup files.
- `models`: Defines the SQLAlchemy models used for database interaction.
"""

# Import and expose key components for easier access throughout the application
from .config.config_loader import load_config
from .config.logging_loader import logger
from .models.base import Base
from .session_manager import AppSession

# Expose app_container for centralized dependency injection if needed
from .config.app_container import AppContainer

__all__ = [
    "load_config",
    "logger",
    "Base",
    "AppContainer",
    "AppSession"
]
