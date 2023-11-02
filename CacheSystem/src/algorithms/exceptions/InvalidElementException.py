class InvalidElementException(Exception):
    """
    Exception raised when an invalid element is accessed.
    """

    def __init__(self, message: str):
        super().__init__(message)
