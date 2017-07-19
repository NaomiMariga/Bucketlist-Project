import unittest
from  models.user import User

class UserTest(unittest.TestCase):  

    def setUp(self):
        self.user = User()

    def test_register_user(self):
        self.assertEqual(self.user.register_user({"username":"Naomi", "password":"12345", "email":"naomi@gmail.com"}), "Account created")
    def test_login_user(self):
        self.assertEqual(self.user.login_user({"username":"Naomi", "password":"12345"}), "logged in successfully")

    
    
