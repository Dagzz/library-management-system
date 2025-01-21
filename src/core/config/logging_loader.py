"""
Provides a utility to configure and return the application logger.
The logger outputs logs to both a file (`app.log`) and the console
with appropriate log levels for each handler.

Usage:
- Import the `setup_logger` function:
    from core.config.logging_loader import setup_logger
- Initialize the logger:
    logger = setup_logger()
"""
import os
import logging
from logging import Logger

def setup_logger() -> Logger:
    """
    Configure and return the logger for the application.

    The logger outputs logs to both a file (WARNING and above)
    and the console (INFO and above), formatted with timestamps 
    and log levels.
    """
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.DEBUG)

    # Ensure the log file path
    log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.log')

    # Format for the logs
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler: Logs are written to 'app.log' | WARNING and above
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(log_format)

    # Console handler: Logs are displayed in the console | INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Instantiate a logger
logger = setup_logger()
