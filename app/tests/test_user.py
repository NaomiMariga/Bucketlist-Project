import unittest
from  models.user import User

class UserTest(unittest.TestCase):  

    def setUp(self):
        self.user = User()

    def test_register_user(self):
        self.assertEqual(self.user.register_user({"fname":"Naomi","oname":"mariga", "email":"naomi@gmail.com","phone":"071852","username":"Naomi", "password":"12345"}), "Account created")
    def test_login_user(self):
        self.assertEqual(self.user.login_user({"username":"Naomi", "password":"12345"}), "logged in successfully")
    def test_invalid_login(self):
        self.assertEqual(self.user.login_user({"username":" ","password":" "}),"Please provide username and password ")
  
    
