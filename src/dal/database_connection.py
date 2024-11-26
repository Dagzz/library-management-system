from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.resources.config.config_loader import load_config

def get_engine():
    '''
    Create and return a SQLAlchemy engine for database connection.

    This function reads the configuration from the `config.ini` file 
    and constructs a connection string to initialize the SQLAlchemy engine.

    :return: A SQLAlchemy engine instance for connecting to the database.
    '''
    config = load_config()
    
    host = config['mysql']['host']
    user = config['mysql']['user']
    password = config['mysql']['password']
    database = config['mysql']['database']

    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

    return create_engine(connection_string)

def get_session():
    '''
    Create and return a new SQLAlchemy session.

    This function initializes a session using the SQLAlchemy engine
    provided by the `get_engine` function, enabling interaction with
    the database for executing queries and transactions.

    :return: A new SQLAlchemy session instance.
    '''
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
