#Safe Square Root
import math
number= int(input("Inserire numero: "))
def safe_sqrt(number):
    try:
        print(math.sqrt(number))
    except  ValueError as error:
        print(error)

safe_sqrt(number)
        
