#class persona

class Persona:

    def __init__(self,name,lastname,age):
        self.setName(name) = name
        self.setLastname(lastname) = lastname
        self.setAge(age) = age

    def getName(self):
        return self.name
    
    def getLastname(self):
        return self.latsname
    
    def getAge(self):
        return self.age
    
    def setName(self, name):
        if name:
            self.name = name
        else:
            print("Error! Il nome non può essere una stringa vuota!")
    
    def setLastname(self, lastname):
        if lastname:
            self.lastname = lastnamename
        else:
            print("Error! Il cognome non può essere una stringa vuota!")

    def speak(self) -> None:
        print(f"\nHello my name is {self.getName()}")
    
    def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lats_name}\nEtà: {self.age}"
    
    

