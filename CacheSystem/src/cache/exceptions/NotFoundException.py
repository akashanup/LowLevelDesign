class NotFoundException(Exception):
    """
    Exception raised when a key is not found.
    """

    def __init__(self, message: str):
        super().__init__(message)