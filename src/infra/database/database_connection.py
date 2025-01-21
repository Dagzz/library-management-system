"""
Provides utilities to set up and manage the database connection and sessions.

Purpose:
- `get_engine`: Creates a single SQLAlchemy engine using database configurations from `config.ini`.
- `get_session`: Initializes and returns a new SQLAlchemy session for executing queries and transactions.

Usage:
- Import the desired function:
    from src.infra.database.database_connection import get_session
- Use `get_session` to interact with the database:
    session = get_session()
"""
from src.core.config.config_loader import load_config
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.core.config.logging_loader import logger

# Initialize the engine once globally
_engine: Engine = None
_SessionLocal: sessionmaker = None

def get_engine() -> Engine:
    """
    Return a singleton SQLAlchemy engine for database connection.

    The engine is created once using the configuration from `config.ini` 
    and reused for subsequent calls.

    :return: A SQLAlchemy engine instance for connecting to the database.
    """
    global _engine
    if _engine is None:
        logger.info("Creating database engine.")
        try:
            config = load_config()
            host = config['mysql']['host']
            user = config['mysql']['user']
            password = config['mysql']['password']
            database = config['mysql']['database']

            connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
            _engine = create_engine(connection_string)
            logger.info("Database engine created successfully.")
        except Exception as e:
            logger.error("Failed to create the database engine.", exc_info=True)
            raise
    return _engine

def get_session() -> Session:
    """
    Create and return a new SQLAlchemy session.

    This function initializes a session using the globally created 
    SQLAlchemy engine, enabling interaction with the database for 
    executing queries and transactions.

    :return: A new SQLAlchemy session instance.
    """
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_engine())

    try:
        logger.info("Creating a new database session.")
        return _SessionLocal()
    except Exception as e:
        logger.error("Failed to create a new database session.", exc_info=True)
        raise
