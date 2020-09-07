import unittest
from credential import Credentials


class TestCredentials(unittest.TestCase):
    """
    Test class for Credentials class
    """

    def setUp(self):
        """
        Method that runs before individual credential test are run
        """
        self.new_credential = Credentials('Gmail', 'Brian-Muchera', 'qwerty')

    def test_init(self):
        """
        Test Case to check if new Credentials are initialised correctly.
        """
        self.assertEqual(self.new_credential.account, "Gmail")
        self.assertEqual(self.new_credential.userName, "Brian-Muchera")
        self.assertEqual(self.new_credential.password, "qwerty")

    def test_save_credential(self):
        """
        Test if credential list has been saved into list
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

         def tearDown(self):
        """
        Clean up after each test case
        """
        Credentials.credentials_list = []

    def test_multiple_account(self):
        """
        Test if multiple accounts can be saved
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "Brian-Muchera", "asdfg")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        """
        Test if account credentials can be removed
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "Brian-Muchera", "asdfg")
        test_credential.save_details()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

