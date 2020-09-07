class User:

    """
    Create User class that gnerates new instances for user.
    """

    user_list = []

    def __init__(self, username, password):
        """
        Method taht defines the properties of a user
        """
        self.username = username
        self.password = password