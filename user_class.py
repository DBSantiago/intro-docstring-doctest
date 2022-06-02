"""
Class User module docstring
"""


class User:
    """
    Represents a program user.
    """

    def __init__(self, username: str, password: str) -> None:
        """
        Instantiates a User object.

        Args:
            username (str): User's username.
            password (str): User's password.

        Returns:
            None: None
        """
        self.username = username
        self.password = password
