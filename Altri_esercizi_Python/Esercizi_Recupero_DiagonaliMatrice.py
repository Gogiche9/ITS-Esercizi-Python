#Somma delle Diagonali di una Matrice

def sum_primary_diagonal(matrice:list[list[int]])-> int:
    indice = 0
    numeri_da_sommare = []
    for liste in matrice:
        numeri_da_sommare.append(liste[indice])
        indice += 1
    somma = 0
    for numeri in numeri_da_sommare:
        somma += numeri
    return print(somma)

def sum_secondary_diagonal(matrice:list[list[int]])-> int:
    indice = -1
    numeri_da_sommare = []
    for liste in matrice:
        numeri_da_sommare.append(liste[indice])
        indice -= 1
    somma = 0
    for numeri in numeri_da_sommare:
        somma += numeri
    return print(somma)


mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

sum_primary_diagonal(mat1)
sum_secondary_diagonal(mat1)