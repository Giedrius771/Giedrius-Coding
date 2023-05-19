import datetime

class Sukaktis:
    def __init__(self, data):
        self.sukaktis1 = data

    def praejo(self):
        data = self.sukaktis1
        dabar = datetime.datetime.now()
        praejo1 = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        skirtumas = dabar - praejo1
        return 'Praėjo metų: ' + str(round(skirtumas.days / 365)) + ', Praėjo mėnesių: ' + str(
            round(skirtumas.days / 30)) + ', Dienų skirtumas: ' + str(skirtumas.days) + ', Praėjo valandų: ' + str(
            round(skirtumas.total_seconds() / 3600)) + ', Praėjo minučių: ' + str(
            round(skirtumas.total_seconds() / 60)) + ', Praėjo sekundžių: ' + str(round(skirtumas.total_seconds()))

    def keliamieji(self):
        data = self.sukaktis1
        praejo1 = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        praejo2 = praejo1.year
        praejo3 = int(praejo2)
        if praejo3 % 400 == 0 or (praejo3 % 4 == 0 and praejo3 % 100 != 0):
            return 'Keliamieji metai'
        else:
            return 'Nekeliamieji metai'

    def atimt(self, days):
        data = self.sukaktis1
        praejo1 = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        praejo2 = praejo1 - datetime.timedelta(days=days)
        return praejo2.strftime('%Y-%m-%d %H:%M:%S')

    def pridet(self, days):
        data = self.sukaktis1
        praejo1 = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        praejo2 = praejo1 + datetime.timedelta(days=days)
        return praejo2.strftime('%Y-%m-%d %H:%M:%S')


sukaktis1 = Sukaktis(input(f"Iveskite data (pvz:2015-01-01 12:00:00): "))
print(sukaktis1.praejo())
print(sukaktis1.keliamieji())
print(sukaktis1.atimt(10))
print(sukaktis1.pridet(10))