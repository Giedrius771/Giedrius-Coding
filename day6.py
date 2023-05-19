# 1 uzduotis ################*************
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f'Automobilis: {self.metai} {self.modelis}, {self.kuro_tipas}')


    def vaziuoti(self):
             print('Vaziuoja')

    def stoveti(self):
                print('Priparkuota')

    def pildyti_degalu(self):
                print('Degalai ipilti')


class Elektromobilis(Automobilis):

    def pildyti_degalu(self):
        print('Baterija ikrauta')

    def vaziuoti_autonomiskai(self):
        print('Vaziuoja automatiskai')

auto = Automobilis(2008, 'Volvo' , 'Dyzelinas')
auto.vaziuoti()
auto.stoveti()
auto.pildyti_degalu()

elektra = Elektromobilis(2021, 'Tesla', 'Elektra')
elektra.vaziuoti()
elektra.stoveti()
elektra.pildyti_degalu()
elektra.vaziuoti_autonomiskai()
## 2 uzduotis ################*************
import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y %m %d")

    def __repr__(self):
        return "Darbuotojas: " + str(self.vardas) + "; valandos_įkainis - " + str(
            self.valandos_ikainis) + "; darbo_pradžia - " + str(self.dirba_nuo.date())

    def dienu_skirtumas(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days // 7 * 7  # apvaliname iki savaitės

    def paskaiciuoti_atlyginima(self):
        dienos = self.dienu_skirtumas()
        atlyginimas = dienos * 8 * self.valandos_ikainis
        print(f"{self.vardas} atlyginimas: {atlyginimas} EUR")


class NormalusDarbuotojas(Darbuotojas):
    def dienu_skirtumas(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days // 7 * 5  # apvaliname iki savaitės


darbuotojas1 = Darbuotojas("Tomas", 7.2, "2013 02 21")
darbuotojas2 = Darbuotojas("Saulius", 5, "2015 07 01")
darbuotojas3 = Darbuotojas("Edgaras", 3.3, "2018 09 01")
darbuotojas4 = Darbuotojas("Marius", 5, "2009 11 17")
print(darbuotojas1)
darbuotojas1.paskaiciuoti_atlyginima()
print(darbuotojas2)

darbuotojas2.paskaiciuoti_atlyginima()
normalus_darbuotojas = NormalusDarbuotojas("Giedrius", 7.5, "2017 09 01")
normalus_darbuotojas.paskaiciuoti_atlyginima()
# 3 uzduotis ################*************
class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.tipas = "Pajamos"
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.tipas = "Išlaidos"
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


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
                print(f"Pajamos: {irasas.suma}, siuntėjas: {irasas.siuntejas}, papildoma informacija: {irasas.papildoma_informacija}")
            elif isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma}, atsiskaitymo būdas: {irasas.atsiskaitymo_budas}, įsigyta prekė/paslauga: {irasas.isigyta_preke_paslauga}")


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