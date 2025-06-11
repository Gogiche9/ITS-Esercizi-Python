#9-15. Lottery Analysis

import random

class LotteryMachine:
    
    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
        self.my_ticket = []

    def draw_winning_ticket(self):
        self.my_ticket = []
        for element in range(4):
            self.my_ticket.append(random.choice(self.list))
        return self.my_ticket
    
    def display_ticket(self):
        print(f"The winning ticket is {self.draw_winning_ticket()}")
        print("Every ticket matching the numbers have won!")

    def simulate_until_win(self, my_ticket):
        counter = 0
        while True:
            new_ticket = self.draw_winning_ticket()
            counter += 1
            if sorted(new_ticket) == sorted(my_ticket):
                return counter, my_ticket
    
machine = LotteryMachine()
my_ticket = machine.draw_winning_ticket()
counter, winning_ticket = machine.simulate_until_win(my_ticket)

print(my_ticket)
print(f"Attempts: {counter}, Winning tickets: {winning_ticket}")

        




        
