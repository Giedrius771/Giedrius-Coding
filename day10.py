class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas


    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas < 0:
            print("Atlyginimas negali būti neigiamas")
        else:
            self.__atlyginimas = naujas_atlyginimas


domas = Darbuotojas("Domas", "Adomaitis", 1200)
print(domas.atlyginimas)  # Access the property without parentheses

domas.atlyginimas = 1500
print(domas.atlyginimas)
##################
class Auto:
    def __init__(self, marke, modeli):
        self.marke = marke
        self.modelis = modeli


a1 = Auto("Audi", "a4")
a2 = Auto("Bmw", "3")
pass