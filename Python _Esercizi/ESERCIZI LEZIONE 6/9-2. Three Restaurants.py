#9-2. Three Restaurants

class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return print(self.restaurant_name, self.cuisine_type)
        
    def open_restaurant(self):
        return print("The restaurant is Open!")

restaurant1 = Restaurant("Er Forno", "cucina tailandese")
restaurant2 = Restaurant("Da Mimmo Er Padellaro", "cucina Fusion")
restaurant3 = Restaurant("'A scarpetta", "cucina Francese")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()