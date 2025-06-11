#Esercizi Classi
#da deepseek

class Person:

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def greetings(self):
        print(f"Greetings, my name is {self.name} {self.surname}, i am {self.age} years old")

'''persona1 = Person("Mario", "Rossi", 30)
persona1.greetings()'''

class Rettangolo:

    def __init__(self,base,altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        area = self.base * self.altezza
        return area
    
    def perimetro(self):
        perimetro = (self.base*2)+(self.altezza*2)
        return perimetro
    
'''rettangolo = Rettangolo(5, 3)
print(rettangolo.area())
print(rettangolo.perimetro())'''

import math
class Cerchio:

    def __init__(self,raggio):
        self.raggio = raggio

    def area(self):
        area = (self.raggio**2)* math.pi
        return "{:.2f}".format(area)
    
    def circonferenza(self):
        circonferenza = 2 * math.pi * self.raggio
        return "{:.2f}".format(circonferenza)
    
'''cerchio1 = Cerchio(5)
print(cerchio1.area())
print(cerchio1.circonferenza())'''

class ContoBancario:

    def __init__(self,nome_titolare,saldo= None):
        self.titolare = nome_titolare
        if saldo == None:
            self.saldo = 0
        else:
            self.saldo = saldo

    def deposita(self,importo):
        self.saldo = self.saldo + importo
        return self.saldo
    
    def preleva(self,importo):
        self.saldo = self.saldo - importo
        return self.saldo
    
    def mostra_saldo(self):
        print(self.saldo)
    
'''conto = ContoBancario("Luigi Verdi")
print(conto.deposita(1000))
print(conto.preleva(300))
conto.mostra_saldo()  # Output: "Saldo attuale: 700"'''

class Libro:

    def __init__(self,titolo,autore,anno_pubblicazione):

        self.disponibile = True
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def presta(self):
        if self.disponibile == True:
            self.disponibile = False
            return self.disponibile
        else:
            print("Libro non disponibile")

    def restituisci(self):
        if self.disponibile == False:
            self.disponibile = True
            return self.disponibile
        else:
            print("Libro già disponibile")

    def descrizione(self):
        print(f"L'autore è: {self.autore}, pubblicato nel: {self.anno_pubblicazione}, il titolo è: {self.titolo}")
        if self.disponibile == True:
            print("Il libro è disponibile")
        else:
            print("Il libro non è disponibile per il prestito")

'''libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954)
libro.presta()
print(libro.disponibile)
libro.descrizione()'''



    

        
        
        
        
