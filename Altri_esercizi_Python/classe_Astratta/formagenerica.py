from abc import ABC, abstractclassmethod

class FormaGenerica(ABC):

    @abstractclassmethod
    def draw(self)-> None:
        pass

    def setShape(self, shape):
        if shape:
            self.shape = shape
        else:
            print("Errore!shape non può essere una stringa vuota!")

    def getShape(self):
        return self.shape



