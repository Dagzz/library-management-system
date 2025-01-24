class DatabaseUpdateError(Exception):
    """Raised when an error occurs while updating the database."""
    def __init__(self, message: str, original_exception: Exception = None):
        super().__init__(message)
        self.original_exception = original_exception

