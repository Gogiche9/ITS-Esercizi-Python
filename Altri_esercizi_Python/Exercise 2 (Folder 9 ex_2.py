#Exercise 2 (Folder 9 ex_2.py)

class Student:

    def __init__(self,name,studyprogram,age,gender):

        self.name = name
        self.studyprogram = studyprogram
        self.age = age
        self.gender = gender

    def printInfo(self):

        print(f"Nome: {self.name}\nProgramma di studi: {self.studyprogram}\nEtà: {self.age}\nGenere: {self.gender}")

yourself = Student("Mirko", "Storia", "26", "m")
leftNeighbour = Student("Leonardo", "Lol", "21", "m")
rightNeighbour = Student("Monica", "Arte e spettacolo", "32", "f")
yourself.printInfo()
leftNeighbour.printInfo()
rightNeighbour.printInfo()
