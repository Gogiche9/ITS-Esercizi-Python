#9-14. Lottery
import random

class LotteryMachine:
    
    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
       
    def select_method(self):
        new_list = []
        for i in range(4):
            new_list.append(random.choice(self.list))
        return new_list

    def winning_ticket(self):
        winning_ticket_list = self.select_method()
        delimiter = ""
        string_list = map(str, winning_ticket_list)
        result = delimiter.join(string_list)
        return result
    
ticket1 = LotteryMachine()
print(ticket1.winning_ticket())


        
            



        