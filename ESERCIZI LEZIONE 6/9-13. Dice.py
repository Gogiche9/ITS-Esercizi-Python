#9-13. Dice

class Dice:

    def __init__(self,sides= 6):
        self.sides = sides

    def roll_dice(self):
        import random
        return random.randint(1,self.sides)

result1 = Dice() 
result2 = Dice(10)
result3 = Dice(20)  
for i in range(10):
    print(result1.roll_dice())
    print(result2.roll_dice())
    print(result3.roll_dice())

    
    



        