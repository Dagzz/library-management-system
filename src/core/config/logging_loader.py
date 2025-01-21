import logging

def setup_logger():
    """
    Configure and return the logger for the application.
    
    The logger outputs logs to both a file and the console.
    """
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.DEBUG)

    # Format for the logs
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler: Logs are written to 'app.log' | WARNING and above
    file_handler = logging.FileHandler("app.log")
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
