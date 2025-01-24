from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Engine, create_engine
from src.core.config.config_loader import load_config
from src.core.config.logging_loader import logger

# Initialize the engine and session maker globally
_engine: Engine = None
_SessionLocal: sessionmaker = None

class CustomSession(Session):
    """
    A custom SQLAlchemy Session that logs when the session is closed.
    """
    def close(self):
        logger.info("Closing the database session.")
        super().close()

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

def get_session() -> CustomSession:
    """
    Create and return a new SQLAlchemy session using the custom session class.

    This function initializes a session using the globally created 
    SQLAlchemy engine, enabling interaction with the database for 
    executing queries and transactions.

    :return: A new CustomSession instance.
    """
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_engine(), class_=CustomSession)

    try:
        logger.info("Creating a new database session.")
        return _SessionLocal()
    except Exception as e:
        logger.error("Failed to create a new database session.", exc_info=True)
        raise