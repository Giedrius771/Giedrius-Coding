from enum import Enum


class IrasoTipas(Enum):
    PAJAMOS = "Pajamos"
    ISLAIDOS = "Išlaidos"


class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas.value}: {self.suma}"


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        self.zurnalas.append(Irasas(IrasoTipas.PAJAMOS, suma))
        print("Pajamos sėkmingai pridėtos!")

    def prideti_islaidu_irasa(self, suma):
        self.zurnalas.append(Irasas(IrasoTipas.ISLAIDOS, suma))
        print("Išlaidos sėkmingai pridėtos!")

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if irasas.tipas == IrasoTipas.PAJAMOS:
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        print("Biudžeto ataskaita:")
        for irasas in self.zurnalas:
            print(irasas)


biudzetas = Biudzetas()

while True:
    print("\nPasirinkite veiksmą:")
    print("1 - Pridėti pajamų įrašą")
    print("2 - Pridėti išlaidų įrašą")
    print("3 - Gauti pajamų ir išlaidų balansą")
    print("4 - Parodyti biudžeto ataskaitą")
    print("5 - Išeiti iš programos")

    pasirinkimas = input("Įveskite pasirinkimą: ")

    if pasirinkimas == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(suma)
    elif pasirinkimas == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(suma)
    elif pasirinkimas == "3":
        balansas = biudzetas.gauti_balansa()
        print(f"Balansas: {balansas}")
    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()
    elif pasirinkimas == "5":
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
