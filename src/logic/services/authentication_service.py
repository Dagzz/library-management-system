from src.core.models.authentication import Authentication
# from werkzeug.security import generate_password_hash TODO implement after
from src.core.session_manager import AppSession
from src.core.custom_exceptions import DatabaseUpdateError

class AuthenticationService:
    def __init__(self, auth_repository, user_repository, role_repository):
        self.authentication_repository = auth_repository
        self.user_repository = user_repository
        self.role_repository = role_repository
        
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
        return auth.id_user

    def set_user_session(self, id_user: int) -> None:
        """
        Put the user's data in the session.
        Retrieves ID, First name, Last name, and Roles.

        Args:
            id_user (int): The ID of the user.
        Raises:
            ValueError: If the user or roles cannot be retrieved.
        """
        try:
            user = self.user_repository.get_user_by_id(id_user)
            if not user:
                raise ValueError(f"User with ID {id_user} not found.")
            
            roles = self.role_repository.get_user_roles(id_user)
            if not roles:
                raise ValueError(f"No roles found for user with ID {id_user}.")
            
            session = AppSession()
            session.set_user(
                user_id=id_user,
                first_name=user.first_name,
                last_name=user.last_name,
                roles=roles
            )
        except Exception as e:
            raise ConnectionError(f"Failed to set user session for user ID {id_user}.") from e

       
    def update_user_last_connection_date(self, id_user):
        """
        Updates the last_connection_date for a user.
        """
        try:
            self.user_repository.update_last_connection_date(id_user)
        except Exception as e:
            # Minor error so we handle it here
            raise DatabaseUpdateError(f"Failed to update last connection date for user ID {id_user}.") from e
        
    def change_user_password(self, id_authentication, new_password):
        """
        Changes the password for a user.
        """
        # hashed_password = generate_password_hash(new_password)
        hashed_password = new_password
        if not self.authentication_repository.change_password(id_authentication, hashed_password):
            raise DatabaseUpdateError("Failed to change password: authentication record not found.")
        return True

    def is_login_available(self, login):
        """
        Checks if the provided login is available.
        """
        return self.authentication_repository.is_login_available(login)
