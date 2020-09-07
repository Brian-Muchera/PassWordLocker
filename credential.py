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

       @classmethod
    def verify_user(cls, username, password):
        """
        Method to verify if in the user_list
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user

    def save_details(self):
        """
        Save new credentials in the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Delete credentials in the credentilas list
        """
        Credentials.credentials_list.remove(self)
  