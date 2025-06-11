#Abstract_class Shape
from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangle(Shape):
    def __init__(self,base,altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza
        
    
    def perimetro(self):
        return (self.base + self.altezza) * 2
        
import math      
class Circle(Shape):
    def __init__(self,raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio**2
    
    def perimetro(self):
        return (math.pi * self.raggio)*2
    
rettangolo1 = Rectangle(20,10)
cerchio1 = Circle(15)

print(rettangolo1.area())
print(rettangolo1.perimetro())
print(cerchio1.area())
print(cerchio1.perimetro())
    

        

