#Esercizi_Recupero_RicercaBinaria

def ricerca_binaria(list_ord:list[int],x:int)->int:
    low = 0
    high = len(list_ord)-1

    while low <= high:
        mid = (low + high)// 2
        if list_ord[mid]< x:
            low = mid + 1
        elif list_ord[mid]> x:
            high = mid - 1
        else:
            return mid
    return -1 #elemento non trovato, siccome deve ritornare int non ho potuto fare un print


list1 = [1,29,33,42,51,65,88]
print(ricerca_binaria(list1, 51))
print(ricerca_binaria(list1, 90))



