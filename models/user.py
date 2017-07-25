"""
vyguu
"""
class User:
    """
    ijiuiui
    """
    def __init__(self):
        self.Registered_users = {}
        self.login = None
    
    def register_user(self,first_name, other_name, email, phone, username, password):
        self.Registered_users = {
            'first_name': first_name,
            'other_name': other_name,
            'email': email,
            'phone': phone,
            'username': username,
            'password': password 
        }
        
    def login_user(self,email,password):
       for email in self.Registered_users:
           if email == email and password == password:
               self.login = email
               

        
           

    