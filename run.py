from user import User
from credential import Credentials


def create_new_user(username, password):
    """
    Create new User with username and password
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Display user
    """
    return User.display_user()


def login_user(username, password):
    """
    Check if user exist and login the user
    """
    check_user = Credentials.verify_user(username, password)
    return check_user


    def create_new_credential(account, userName, password):
    """
    Create new user credentials for a user
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Save credentials to list
    """
    credentials.save_details()


def display_accounts_details():
    """
    returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def search_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.search_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.existing_credential(account)

