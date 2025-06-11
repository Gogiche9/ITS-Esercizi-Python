#class persona

class Persona:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.lats_name = last_name
        self.age = age

    def get_name(self):
        return self.first_name
    
    def get_surname(self):
        return self.lats_name
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lats_name}\nEtà: {self.age}"
    
    

