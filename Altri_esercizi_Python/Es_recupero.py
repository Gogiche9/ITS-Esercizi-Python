#Esercizi recupero lista di tuple

def dizionarioTupla(tupla):

    index = 1
    diz = {}
    for i in tupla:
        if i not in diz:
            diz[i] = tupla[1]
            index += 2
    return diz



def negPos_filter(lista):

    diz = {}
    diz["pos"]= []
    diz["neg"]= []

    for i in lista:
        if i not in diz:
            if i >= 0 :
                diz["pos"].append(i)
            else:
                diz["neg"].append(i)
    return diz

lista = (1,-1,10,-10,3,-3,0,10,-3)
dizionario: dict = negPos_filter(lista)
print(dizionario)

def select_product(dizionario):
    new_dict = {}

    for k,v in dizionario.items():
        if v < 50:
            new_dict[k] = round(((v * 10)/100) + v,2)
    return new_dict

dict_1 = {"roba":49, "grog":100,"costoso":10000}
dict_2 = select_product(dict_1)
print(dict_2)

        

    



