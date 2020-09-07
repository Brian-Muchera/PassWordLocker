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

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

    def main():
    print("Welcome to the PassWordLocker...\n Please the code to navigate through the application.\n NA ---  New Account  \n EA ---  Existing Account  \n")
    nav_code = input("").lower().strip()
    if nav_code == "na":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - Type pasword:\n GP - Generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Incorrect password please try again!!!")
        save_user(create_new_user(username, password))
        print("*"*85)
        print(
            f"Hello {username}, Account created succesfully! Your password is: {password}")
        print("*"*85)
