#users.py

class User:

    def __init__(self,first_name, last_name, username,email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        return print(f"name: {self.first_name}\nlast_name: {self.last_name}\nusername: {self.username}\nemail: {self.email}")

    def greet_user(self):
        return print(f"Salve {self.last_name}{self.first_name}")
    
class Privileges:
    
    def __init__(self,role):
        self.role = role
    
    def show_privileges(self):
        return print(f"Il tuo ruolo è: {self.role}")
    
class Admin:
    
    def __init__(self,user: User,privileges: Privileges):
        self.user = user
        self.privileges = privileges 
        
    def show_information(self):
        self.user.describe_user()
        self.privileges.show_privileges()


    


    

        
    