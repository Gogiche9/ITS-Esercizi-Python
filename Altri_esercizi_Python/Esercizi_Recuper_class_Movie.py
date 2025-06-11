#Esercizi_Recuper_class_Movie

class Movie:

    def __init__(self,movie_id:str,title:str,director:str):
        self.is_rented: bool = False
        self.movie_id = movie_id
        self.title = title
        self.director = director

    def rent(self):
        if self.is_rented == False:
            self.is_rented = True
        else:
            return f"Il film '{self.title}' è già stato noleggiato."
    
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented == False
        else:
            return f"Il film '{self.title}' non è stato noleggiato da questo cliente."

class Customer:

    def __init__(self,customer_id:str,name:str):
        self.rented_movies:list[Movie] = []
        self.customer_id= customer_id
        self.name = name

    def rent_movie(self,movie:Movie):
        if movie not in self.rented_movies:
            self.rented_movies.append(movie)
        else:
            return f"Il film '{movie.title}' è già noleggiato."
        
    def return_movie(self,movie:Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            return f"Il film '{movie.title}' non è stato noleggiato da questo cliente."

class VideoRentalStore:
    def __init__(self):
        self.movie: dict[str,Movie] = {}
        self.customer:dict[str,Customer] = {}

    def add_movie(self,movie_id:str,title:str,director:str):
        if movie_id in self.movie:
            self.movie[movie_id] = Movie(movie_id,title,director)
        else:
            return f"Il film con ID '{movie_id}' esiste già."
    
    def register_customer(self,customer_id: str, name: str):
        if customer_id not in self.customer:
            self.customer[customer_id] = Customer(customer_id,name)
        else:
            return f"Il cliente con ID '{customer_id}' è già registrato."
    
    def rent_movie(self,customer_id: str, movie_id: str):
        if customer_id in self.movie and movie_id in self.customer:
            Customer.rent_movie(movie_id)
        else:
            return f"Cliente o film non trovato."



        



        
    


        

