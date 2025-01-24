from src.core.config.logging_loader import logger

class AppSession:
    """
    A Singleton class to store user session information during the app's lifecycle.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppSession, cls).__new__(cls, *args, **kwargs)
            cls._instance.user_id = None
            cls._instance.first_name = None
            cls._instance.last_name = None
            cls._instance.roles = []
        return cls._instance

    def set_user(self, user_id: int, first_name: str, last_name: str, roles: list[str]):
        """
        Set user details in the session.
        """
        logger.info(f'Saving user data in the session.')
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.roles = roles

    def clear_session(self):
        """
        Clear the session information when the user logs out.
        """
        logger.info(f'Clearing the user\'s session.')
        self.user_id = None
        self.first_name = None
        self.last_name = None
        self.roles = []
