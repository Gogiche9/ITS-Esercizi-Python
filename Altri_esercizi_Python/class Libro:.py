class Libro:

    def __init__(self,titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.prestito = True

        def getTitolo(self):
            return self.titolo
        
        def getAutore(self):
            return self.autore
        
        def getStatoPrestito(self):
            return self.prestito
        
        def setStatoPrestito(self):
            self.prestito = not self.prestito
        

class biblioteca:

    def __init__(self):
        self.catalogo = {}

    def aggiungi_libro(self,libro):
        if libro not in self.catalogo:
            self.catalogo[libro]
        else:
            print(f"{libro} già presente in catalogo")

    def presta_libro(self,titolo):
        if titolo in self.catalogo:
            Libro.getStatoPrestito()


        
        