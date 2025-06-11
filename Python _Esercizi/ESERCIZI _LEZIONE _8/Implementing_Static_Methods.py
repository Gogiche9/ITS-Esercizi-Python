#Implementing_Static_Methods

class MathOperations:

    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
print(MathOperations.add(2,4))
print(MathOperations.multiply(2,4))