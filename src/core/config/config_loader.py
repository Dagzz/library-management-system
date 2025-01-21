"""
Provides a utility to load and parse the application configuration
from the `config.ini` file. Centralizes configuration management 
to ensure consistency and reduce redundancy.

Usage:
- Import the `load_config` function:
    from core.config.config_loader import load_config
- Retrieve the configuration as a `ConfigParser` object:
    config = load_config()
"""

import os
from configparser import ConfigParser
from src.core.config.logging_loader import logger

def load_config() -> ConfigParser:
    '''
    Load and return the configuration from the `config.ini` file.

    This function locates the `config.ini` file in the same directory as this script,
    reads its content using the `ConfigParser` module, and returns the configuration
    as a `ConfigParser` object for further use.

    :return: A `ConfigParser` object containing the configuration loaded from `config.ini`.
    :raises: SystemExit if the configuration file cannot be loaded.
    '''
    
    logger.info('Loading configuration from config.ini')
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config = ConfigParser()
        config.read(config_path)
        
        if not config.sections():
            raise ValueError(f"Configuration file is empty or improperly formatted: {config_path}")

        logger.info(f'Configuration loaded successfully from {config_path}')
        return config

    except FileNotFoundError:
        logger.critical(f'Configuration file not found at {config_path}')
        raise SystemExit(1)

    except Exception as e:
        logger.critical(f'Unexpected error while loading configuration: {e}')
        raise SystemExit(1)

