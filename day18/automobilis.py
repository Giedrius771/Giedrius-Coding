class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.greitis = 0

    def vaziuoti(self):
        return 'Vaziuoja'

    def stoveti(self):
        return 'Priparkuota'

    def pildyti_degalu(self):
        if self.kuro_tipas == 'Elektra':
            return 'Baterija ikrauta'
        else:
            return 'Degalai ipilti'

    def greicio_padidejimas(self, padidinimas):
        self.greitis += padidinimas
        return self.greitis

    def greicio_sumazinimas(self, sumazinimas):
        self.greitis -= sumazinimas
        return self.greitis

    def gauti_informacija(self):
        return self.metai, self.modelis, self.kuro_tipas

    def vaziuoti_autonomiskai(self):
        if self.kuro_tipas == 'Elektra':
            return 'Vaziuoja automatiskai'
        else:
            return 'Negalima vaziuoti autonomiškai'
