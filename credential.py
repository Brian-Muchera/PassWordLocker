import random
import string
import pyperclip
from user import User


class Credentials():
    """
    Create a new Credentials class to create new objects
    """

    credentials_list = []

    def __init__(self, account, userName, password):
        """
        Method to define credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password