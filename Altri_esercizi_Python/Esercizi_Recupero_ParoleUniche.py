#Esercizio Recupero Parole Uniche 
import re
def words_counter(stringa:str)->dict:

    #riduco la stringa in minuscolo
    stringaMinuscola = stringa.lower()

    #rimuovo la punteggiatura
    stringaSenzaPunt = re.sub(r'[^\w\s]', '', stringaMinuscola)

    #suddivito la stringa in base agli spazi bianchi
    lista = stringaSenzaPunt.split()
    
    print(lista)

    contatoreParole = {}
    for token in lista:
        new_word = token
        if new_word not in contatoreParole:
            contatoreParole[new_word] = 1
        else:
            contatoreParole[new_word] += 1
    return contatoreParole

text = "Hello, world! Hello... PYTHON? world."
output = print(words_counter(text))             
    
    




