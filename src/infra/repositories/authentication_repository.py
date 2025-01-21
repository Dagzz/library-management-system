"""
AuthenticationRepository

Handles database operations related to the `Authentication` model.

Responsibilities:
- Managing user authentication data (e.g., login, hashed passwords).
- Fetching authentication details by ID or login.
- Verifying login availability.
- Registering new authentication records.
- Updating hashed passwords.

Usage:
- Initialize with a session factory:
    repo = AuthenticationRepository(get_session)
- Use the provided methods for CRUD and authentication-related queries.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import Optional
from src.core.models.authentication import Authentication
# from werkzeug.security import check_password_hash  # TODO: Implement hashing after

class AuthenticationRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def get_authentication_by_id(self, id_authentication: int) -> Optional[Authentication]:
        """
        Fetch authentication details by ID.
        
        :param id_authentication: The ID of the authentication record.
        :return: The authentication record, or None if not found.
        """
        session = self.session_factory()
        try:
            return session.query(Authentication).filter(Authentication.id_authentication == id_authentication).one()
        except NoResultFound:
            return None
        finally:
            session.close()

    def authenticate_user(self, login: str, password: str) -> Optional[Authentication]:
        """
        Authenticate a user by their login and password.
        
        :param login: The login credential (e.g., username or email).
        :param password: The plain text password.
        :return: The authentication record if credentials are valid, else None.
        """
        session = self.session_factory()
        try:
            auth = session.query(Authentication).filter(Authentication.login == login).one()
            
            if auth.hashed_password == password:  # Replace with password hashing
                return auth
            return None
        except NoResultFound:
            return None
        finally:
            session.close()

    def is_login_available(self, login: str) -> bool:
        """
        Check if a login is available.
        
        :param login: The login to check.
        :return: True if the login is available, False otherwise.
        """
        session = self.session_factory()
        try:
            auth = session.query(Authentication).filter(Authentication.login == login).first()
            return auth is None
        finally:
            session.close()

    def register_authentication(self, auth: Authentication) -> Authentication:
        """
        Register a new authentication record.
        
        :param auth: The authentication object to register (password should already be hashed).
        :return: The created authentication object.
        """
        session = self.session_factory()
        try:
            session.add(auth)
            session.commit()
            return auth
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def change_password(self, id_authentication: int, new_hashed_password: str) -> bool:
        """
        Change the password for an authentication record.
        
        :param id_authentication: The ID of the authentication record.
        :param new_hashed_password: The new hashed password.
        :return: True if the password was successfully changed, False otherwise.
        """
        session = self.session_factory()
        try:
            auth = session.query(Authentication).filter(Authentication.id_authentication == id_authentication).one_or_none()
            if auth:
                auth.hashed_password = new_hashed_password
                session.commit()
                return True
            return False
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
