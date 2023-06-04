from PajamuIrasasC import PajamuIrasas
from islaiduIrasasc import IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        self.zurnalas.append(PajamuIrasas(suma, siuntejas, papildoma_informacija))
        print("Pajamos sėkmingai pridėtos!")

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.zurnalas.append(IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga))
        print("Išlaidos sėkmingai pridėtos!")

    def gauti_balansa(self):
        pajamos = 0
        islaidos = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                pajamos += irasas.suma
            elif isinstance(irasas, IslaiduIrasas):
                islaidos += irasas.suma
        return pajamos - islaidos

    def parodyti_ataskaita(self):
        print("Biudžeto ataskaita:")
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(
                    f"Pajamos: {irasas.suma}, siuntėjas: {irasas.siuntejas}, papildoma informacija: {irasas.papildoma_informacija}")
            elif isinstance(irasas, IslaiduIrasas):
                print(
                    f"Išlaidos: {irasas.suma}, atsiskaitymo būdas: {irasas.atsiskaitymo_budas}, įsigyta prekė/paslauga: {irasas.isigyta_preke_paslauga}")


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
        suma = float(input("Įveskite sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)

    elif pasirinkimas == "2":
        suma = float(input("Įveskite sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę/paslaugą: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)

    elif pasirinkimas == "3":
        balansas = biudzetas.gauti_balansa()
        print(f"Pajamų ir išlaidų balansas: {balansas}")

    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()

    elif pasirinkimas == "5":
        break

    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
