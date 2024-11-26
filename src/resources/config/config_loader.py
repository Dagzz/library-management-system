import os
from configparser import ConfigParser

def load_config():
    '''
    Load and return the configuration from the `config.ini` file.

    This function locates the `config.ini` file in the same directory as this script,
    reads its content using the `ConfigParser` module, and returns the configuration
    as a `ConfigParser` object for further use.

    :return: A `ConfigParser` object containing the configuration loaded from `config.ini`.
    '''
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = ConfigParser()
    config.read(config_path)
    return config
