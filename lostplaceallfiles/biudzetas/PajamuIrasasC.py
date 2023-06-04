from IrasasC import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.tipas = "Pajamos"
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
