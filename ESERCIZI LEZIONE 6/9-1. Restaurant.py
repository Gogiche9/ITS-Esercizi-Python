#9-1. Restaurant

class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return print(self.restaurant_name, self.cuisine_type)
        
    def open_restaurant(self):
        return print("The restaurant is Open!")

restaurant = Restaurant("Er Forno", "cucina tailandese")
restaurant.describe_restaurant()
restaurant.open_restaurant()





       
        