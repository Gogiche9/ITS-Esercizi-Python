class movieCatalog:

    def __init__(self):
        self.catalog = {}

    def add_movie(self,director_name, movies):
        if director_name not in self.catalog:
            self.catalog[director_name] = movies
        else:
            if movies in self.catalog:
                print("Film già presente nella lista")
            else:
                self.catalog[director_name].append(movies)
    
    def remove_movie(self,director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if len(self.catalog[director_name]) == 0:
                    self.catalog.remove(director_name)
            else:
                print(f"{movie_name} non è nel catalogo")

    def  list_directors(self):
        for k,v in self.catalog.items():
            print(f"Lista registi: {k}")

    def get_movies_by_director(self,director_name):
        if director_name in self.catalog:
            print(self.catalog[director_name])
        else:
            print(f"Il regista {director_name} non è in lista")
    
    def search_movies_by_title(self,title):
        found_movies = {}
        for k,v in self.catalog:
            if title.lower() in k.lower() or v.lower():
                found_movies[k] = v
        return found_movies
    



            



       

    
        

                
        