class User:
    def __init__(self):
        self.Registered_users = {}
        self.login = None
    
    def register_user(self,fname,oname,email,phone,username,password):
        self.Registered_users = {
            'first_name': fname,
            'other_name': oname,
            'email': email,
            'phone': phone,
            'username': username,
            'password': password 
        }
        
    def login_user(self,email,password):
       for email in self.Registered_users:
           if email == email and password == password:
               self.login = email
               

        
           

    