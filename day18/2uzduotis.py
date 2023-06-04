import unittest
from automobilis import Automobilis


class TikrintiAutomobilis(unittest.TestCase):
    def setUp(self):
        self.auto = Automobilis(2008, 'Volvo', 'Dyzelinas')

    def test_vaziuoti(self):
        self.assertEqual(self.auto.vaziuoti(), 'Vaziuoja')

    def test_stoveti(self):
        self.assertEqual(self.auto.stoveti(), 'Priparkuota')

    def test_pildyti_degalu(self):
        self.assertEqual(self.auto.pildyti_degalu(), 'Degalai ipilti')

    def test_greicio_padidejimas(self):
        self.auto.greitis = 50
        self.assertEqual(self.auto.greicio_padidejimas(20), 70)
        self.assertEqual(self.auto.greicio_padidejimas(30), 100)
        self.assertEqual(self.auto.greicio_padidejimas(10), 110)

    def test_greicio_sumazinimas(self):
        self.auto.greitis = 100
        self.assertEqual(self.auto.greicio_sumazinimas(50), 50)
        self.assertEqual(self.auto.greicio_sumazinimas(30), 20)
        self.assertEqual(self.auto.greicio_sumazinimas(10), 10)


class TestElektromobilis(unittest.TestCase):
    def setUp(self):
        self.elektra = Automobilis(2021, 'Tesla', 'Elektra')

    def test_pildyti_degalu(self):
        self.assertEqual(self.elektra.pildyti_degalu(), 'Baterija ikrauta')

    def test_pildyti_degalu2(self):
        elektra = Automobilis(2022, 'Tesla', 'Elektra')
        self.assertEqual(elektra.pildyti_degalu(), 'Baterija ikrauta')

    def test_vaziuoti_autonomiskai(self):
        self.assertEqual(self.elektra.vaziuoti_autonomiskai(), 'Vaziuoja automatiskai')

    def test_gauti_informacija(self):
        self.assertEqual(self.elektra.gauti_informacija(), (2021, 'Tesla', 'Elektra'))
