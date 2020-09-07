import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """


    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('brian', 'muchera' 'steph1')