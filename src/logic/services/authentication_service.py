from src.infra.repositories.authentication_repository import AuthenticationRepository
from src.core.models.authentication import Authentication
# from werkzeug.security import generate_password_hash TODO implement after

class AuthenticationService:
    def __init__(self, repository):
        self.authentication_repository = repository

    def register_user(self, id_user, login, password):
        """
        Registers a new user for authentication.
        Business logic: ensure unique login, hash password.
        """
        if not self.authentication_repository.is_login_available(login):
            raise ValueError(f"Login '{login}' is already taken.")

        # hashed_password = generate_password_hash(password)
        hashed_password = password
        new_auth = Authentication(
            id_user=id_user,
            login=login,
            hashed_password=hashed_password
        )
        return self.authentication_repository.register_authentication(new_auth)

    def authenticate_user(self, login, password):
        """
        Authenticates a user by their login and password.
        Returns the authentication record if successful.
        """
        auth = self.authentication_repository.authenticate_user(login, password)
        if not auth:
            raise ValueError("Invalid login or password.")
        return auth

    def change_user_password(self, id_authentication, new_password):
        """
        Changes the password for a user.
        """
        # hashed_password = generate_password_hash(new_password)
        hashed_password = new_password
        if not self.authentication_repository.change_password(id_authentication, hashed_password):
            raise ValueError("Failed to change password: authentication record not found.")
        return True

    def is_login_available(self, login):
        """
        Checks if the provided login is available.
        """
        return self.authentication_repository.is_login_available(login)
