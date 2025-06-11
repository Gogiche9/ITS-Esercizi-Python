#Book_Class

class Book:
    def __init__(self,title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Il titolo è: {self.title}\nL'autore è: {self.author}\nL'ISBN è: {self.isbn}"

    def from_string(cls, stringa):
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip(),lista[2].strip())
    
class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_books(self):
        return self.borrowed_books.append(self.name)
    
    def return_books(self):
        return self.borrowed_books.remove(self.name)
    
    def __str__(self):
        return f"Name: {self.name}\nMember_id: {self.member_id}"
    
    def from_string(cls, stringa):
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip())
    
class Library:

    def __init__(self,books,member):
        self.books = books
        self.member = member
        self.total_books = 0
        self.library = {}

    def add_book(self):
        self.library["book"] = self.books
        self.total_books += 1

    def remove_book(self):
        for k,v in self.library.items():
            if k == "book":
                

        


    
        


        
        