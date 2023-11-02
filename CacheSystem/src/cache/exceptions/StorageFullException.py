class StorageFullException(Exception):
    """
        Exception raised when storage is full.
        """

    def __init__(self, message: str):
        super().__init__(message)