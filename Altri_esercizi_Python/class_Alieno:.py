class Alieno:

    def __init__(self,galaxy: str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self,galaxy):
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia di provenienza non può essere una stringa vuota!")
        
    def getGalaxy(self)-> None:
        return self.galaxy
    
    def speak(self)-> None:
        print("iva vlad iva nul vampir")

    def __str__(self):
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}"

        