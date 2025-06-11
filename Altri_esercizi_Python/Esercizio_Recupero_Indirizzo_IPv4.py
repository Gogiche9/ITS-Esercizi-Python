#Esercitazione Indirizzo IPv4

def is_valid_ipv4(address: str) -> bool:

    #numero corretto punti 
    num_punti = 0
    corretto = True
    for i in address:
        if i == ".":
            num_punti += 1
    if num_punti != 3:
        corretto = False
    
    #suddivido la stringa in base ai punti
    lista_suddivisa_per_punti = address.split(".")
    print(lista_suddivisa_per_punti)
    
    #trasformo in interi le stringhe nella lista
    lista_interi = []
    for i in lista_suddivisa_per_punti:
        intero = int(i)
        lista_interi.append(intero)
    print(lista_interi)

    #controllo siano in range 0-255
    for element in lista_interi:
        if element not in range(0,256):
            corretto = False
    
    #controllo che vi siano 4 parti numeriche
    if len(lista_suddivisa_per_punti) != 4:
        corretto = False
    
    #controllo che siano solo cifre
    for element in lista_suddivisa_per_punti:
        if element.isdigit() == False:
            corretto = False
        
    return print(corretto)

    
is_valid_ipv4("192.168.001.001")
is_valid_ipv4("192.168.0.1")
is_valid_ipv4("255.255.255.255")
is_valid_ipv4("256.100.10.1")
is_valid_ipv4("192.168.1")
is_valid_ipv4("192.168.1.a")

    
    
        
    
