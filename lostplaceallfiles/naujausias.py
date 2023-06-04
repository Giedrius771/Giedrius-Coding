class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulas_tekstas(self):
        return self.tekstas[::-1]

    def mazosios_tekstas(self):
        return self.tekstas.lower()

    def didziosios_tekstas(self):
        return self.tekstas.upper()

    def zodis_pagal_eile(self):
        return self.tekstas.split()

    def simboliu_skaicius(self):
        return len(self.tekstas)

    def skaiciuoti_simbolius(self, simbolis):
        return self.tekstas.count(simbolis)

    def skaiciuoti_zodzius(self, zodis):
        return self.tekstas.count(zodis)

    def get_zodis_numeris(self, seq_num, word):
        words = self.tekstas.split()
        if seq_num >= len(words):
            return None
        if words[seq_num] == word:
            return seq_num
        return -11111

    def pakeisti_zodi(self, old_word, new_word):
        words = self.tekstas.split()
        if old_word not in words:
            return self.tekstas
        else:
            new_text = ' '.join([new_word if w == old_word else w for w in words])
            return new_text

    def skaiciuoti(self):
        num_words = len(self.tekstas.split())
        num_digits = sum(1 for char in self.tekstas if char.isdigit())
        num_uppercase = sum(1 for char in self.tekstas if char.isupper())
        num_lowercase = sum(1 for char in self.tekstas if char.islower())
        return num_words, num_digits, num_uppercase, num_lowercase


kintamasis = Sakinys("Siandien yra sestadienis")
print(kintamasis.tekstas)
print(kintamasis.atbulas_tekstas())
print(kintamasis.mazosios_tekstas())
print(kintamasis.didziosios_tekstas())
"""print(kintamasis.zodis_pagal_eile())"""
print(kintamasis.simboliu_skaicius())

numeris = kintamasis.get_zodis_numeris(1, 'Siandien')
print(numeris)
print(kintamasis.skaiciuoti_simbolius('i'))
print(kintamasis.skaiciuoti_zodzius('yra'))
pakeisti = kintamasis.pakeisti_zodi('yra', 'buvo')
print(pakeisti)
num_words, num_digits, num_uppercase, num_lowercase = kintamasis.skaiciuoti()
print(f"Number of words: {num_words}")
print(f"Number of digits: {num_digits}")
print(f"Number of uppercase letters: {num_uppercase}")
print(f"Number of lowercase letters: {num_lowercase}")