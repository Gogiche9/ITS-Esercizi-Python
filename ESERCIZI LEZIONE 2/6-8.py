#6-8

chameleon = {"type" : "reptile", "name" : "Carlos", "owner" : "Franco"}

bunny = {"type" : "rodent", "name" : "Jorge", "owner" : "Caloggero"}

monkey = {"type" : "ape", "name" : "Juan", "owner" : "Alcite"}

pets = [chameleon, bunny, monkey]

for i in pets:

    for k,v in i.items():

        print(k, v)

