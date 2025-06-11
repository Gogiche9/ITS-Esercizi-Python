#Esercizi_Recupero_Funzioni

def condictionSatisfied(X,Y,Z):
    if X and (Y or Z):
        return f"condiction satisfied"
    else:
        return f"condiction not satisfied"
    
def thresholdMultiplier(lista_interi,threshold):
    new_list= []
    moltiplication = 1

    for i in lista_interi:
        if type(i) == int and i < threshold:
            new_list.append(i)
        for i in new_list:
            moltiplication *= i
    return moltiplication

def cyclesequence():

    for i in range (2,15,2):
        print(i)
    for i in range(1,14,3):
        print(i)
    for i in range(30,-1,-5):
        print(i)
    for i in range(5,46,10):
        print(i)
    

cyclesequence()

#es extra calcola fattoriale

def fattoriale(n:int)->int:
    fattoriale = 1
    while n > 0:
        fattoriale *= n
        n -= 1
    return fattoriale

#print(fattoriale(100))
        

    





