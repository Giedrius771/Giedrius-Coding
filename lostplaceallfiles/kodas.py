import datetime

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y %m %d")

    def __repr__(self):
        return "Darbuotojas: " + str(self.vardas) + "; valandos įkainis - " + str(
            self.valandos_ikainis) + "; darbo pradžia - " + str(self.dirba_nuo.date())

    def dienu_skirtumas(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days // 7 * 7  # apvaliname iki savaites

    def paskaiciuoti_atlyginima(self):
        dienos = self.dienu_skirtumas()
        atlyginimas = dienos * 8 * self.valandos_ikainis
        print(f"{self.vardas} atlyginimas: {atlyginimas} EUR")

class NormalusDarbuotojas(Darbuotojas):
    def dienu_skirtumas(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days // 7 * 5  # apvaliname iki savaites

darbuotojas1 = Darbuotojas("Petras", 7, "2023 01 03")
darbuotojas2 = Darbuotojas("Antanas", 5, "2023 01 03")
print(darbuotojas1)
darbuotojas1.paskaiciuoti_atlyginima()
print(darbuotojas2)
darbuotojas2.paskaiciuoti_atlyginima()
normalus_darbuotojas = NormalusDarbuotojas("Jonas", 10, "2001 11 13")
normalus_darbuotojas.paskaiciuoti_atlyginima()
