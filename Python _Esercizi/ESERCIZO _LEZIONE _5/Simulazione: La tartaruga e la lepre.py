#Simulazione: La tartaruga e la lepre
import random
def percorso():
    percorso = ['_'] * 70
    percorso[0] = "H and T"
    percorso[-1] = "arrivo"
    return percorso

def tortoise_move():
    i =random.randint(1,10)
    if 1 <= i <= 5:
        print("tartaruga passo veloce")
        percorso[position - 1] = "'_'"
        position += 3
        percorso[position -1] = "T"
    elif 6 <= i <= 7 and position >= 1:
        print("tartaruga scivolata")
        percorso[position - 1] = "'_'"
        position -= 6
        if position < 1:
            position = 1
        percorso[position -1] = "T"
    elif 8 <= i <= 10:
        print("tartaruga passo lento")
        percorso[position - 1] = "'_'"
        position += 1
        percorso[position - 1] = "T"
    else:
        position = 1
        percorso[0] = "T"
            

def hare_move():
    i =random.randint(1,10)
    if 1 <= i <= 2:
        print("Lepre riposo")
    elif 3 <= i <= 4:
        print("Lepre Grande Balzo")
        percorso[position - 1] = "'_'"
        position += 9
        percorso[position -1] = "H"
    elif 5 <= i and i >= 1:
        print("Lepre grande scivolata")
        percorso[position - 1] = "'_'"
        position -= 12
        if position < 1:
            position = 1
        percorso[position - 1] = "T"
    else:
        position = 1
        percorso[0] = "H"


    


    
    
    
    

