#9-4._Number Served

class Restaurant:

    def __init__(self,restaurant_name,cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        return print(f"{self.restaurant_name}\n{self.cuisine_type}\nClienti serviti: {self.number_served}")
        
    def open_restaurant(self):
        return print("The restaurant is Open!")
    
    def set_number_served(self, number):
        self.number_served = number

    def  increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("Er Forno", "cucina tailandese", 44)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(22)
restaurant.increment_number_served(6)
restaurant.describe_restaurant()




        

