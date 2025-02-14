#esercizio 1-6 modulo 2

somma = 0

itsMenu = {"Pizza" : 9.00, 
           "Pasta" : 10.50,
           "Zuppa" : 7.00,
           "Hamburger" : 15.50,
           "Cotoletta" : 10.00,
           "Salmone" : 20.20,
           "Patatine Fritte" : 5.50,
           "Patate al Forno" : 5.50,
           "Verdura del giorno" : 7.00,
           "Cheesecake" : 6.00,
           "Tiramisù" : 6.00,
           "Focaccia con Nutella" : 6.00,
           "Coca Cola" : 3.50,
           "Acqua" : 1.50,
           "Vino" : 5.00}



ordine = [itsMenu["Zuppa"], itsMenu["Salmone"], itsMenu["Coca Cola"]]

print(ordine)

for i in ordine:

    somma = somma + i

print(somma)

