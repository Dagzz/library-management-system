"""
Provides utilities to set up and manage the database connection and sessions.

Purpose:
- `get_engine`: Creates a SQLAlchemy engine using database configurations from `config.ini`.
- `get_session`: Initializes and returns a new SQLAlchemy session for executing queries and transactions.

Usage:
- Import the desired function:
    from src.infra.database.database_connection import get_session
- Use `get_session` to interact with the database:
    session = get_session()
"""
from src.core.config.config_loader import load_config
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

def get_engine() -> Engine:
    '''
    Create and return a SQLAlchemy engine for database connection.

    This function reads the configuration from the `config.ini` file 
    and constructs a connection string to initialize the SQLAlchemy engine.

    :return: A SQLAlchemy engine instance for connecting to the database.
    '''
    try:
        config = load_config()
        
        host = config['mysql']['host']
        user = config['mysql']['user']
        password = config['mysql']['password']
        database = config['mysql']['database']

        connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        logger.info("Creating database engine.")
        
        return create_engine(connection_string)
    except Exception as e:
        logger.error("Failed to create the database engine.", exc_info=True)
        raise  # Re-raise the exception after logging it.

def get_session():
    '''
    Create and return a new SQLAlchemy session.

    This function initializes a session using the SQLAlchemy engine
    provided by the `get_engine` function, enabling interaction with
    the database for executing queries and transactions.

    :return: A new SQLAlchemy session instance.
    '''
    try:
        engine = get_engine()
        Session = sessionmaker(bind=engine)
        logger.info("Session created successfully.")
        return Session()
    except Exception as e:
        logger.error("Failed to create a new database session.", exc_info=True)
        raise  # Re-raise the exception after logging it.
