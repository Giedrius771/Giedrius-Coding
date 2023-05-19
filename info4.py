"""def pasisveikinti():
    print("Sveikas pasauli!")

pasisveikinti()
pasisveikinti()
pasisveikinti()

def pasisveikinti(vardas):
    print(f"Sveikas {vardas}")

pasisveikinti("Tomas")
pasisveikinti("Marius")
pasisveikinti("Petras")

def kvadratas(skaicius):
    kvadratu = skaicius ** 2
    print(kvadratu)

kvadratas(4)"""

"""def kvadratu(skaicius):
    rezultatas = skaicius ** 2
    return rezultatas

daugyba = kvadratu(3) * 2
print(daugyba)"""

"""def skaiciu_suma(skaicius1, skaicius2, skaicius3):
    suma = skaicius1 + skaicius2
    daugyba = suma * skaicius3
    return daugyba

print(skaiciu_suma(2, 5, 20))"""

"""def skaiciu_suma(skaicius1, skaicius2, skaicius3=1):
    rezultatas = (skaicius1 + skaicius2) * skaicius3
    return rezultatas

print(skaiciu_suma(2, 5, 4))
print(skaiciu_suma(2, 5))
"""

"""def skaiciu_suma(skaicius1=10, skaicius2=10, skaicius3=1):
    rezultatas = (skaicius1 + skaicius2) * skaicius3
    return rezultatas

print(skaiciu_suma(skaicius3=3))
print(skaiciu_suma(skaicius1=20, skaicius3=3))"""

"""def daug_kvadratu(*args):
    for skaicius in args:
        print(skaicius ** 2)

daug_kvadratu(4, 5, 6, 7, 8, 9, 10)"""

"""def spausdinti_reiksmes(**kwargs):
    for raktas, reiksme in kwargs.items():
        print(raktas, reiksme)
"""


"""spausdinti_reiksmes(vardas="Tomas", lytis="Vyras", amzius=29, daiktai=["Telefonas", "Ausines", "Kuprine"])"""

"""def spausdinti_reiksmes(vardas, pavarde, **kwargs):
    print(f"Vardas: {vardas}, Pavarde: {pavarde}")
    for raktas, reiksme in kwargs.items():
        print(raktas, reiksme)

spausdinti_reiksmes("Tomas", "Runkelis", lytis="Vyras", amzius=29, daiktai=["Telefonas", "Ausines", "Kuprine"])"""


"""def spausdinti_reiksmes(skaicius1, skaicius2, *args):
    print("Skaiciu suma: ", skaicius1 + skaicius2)
    for vienas in args:
        print(vienas)


spausdinti_reiksmes(5, 2, "Labas", 5.25)"""

"""def kvadratu(a):
    return a ** 2
kvadratu = lambda a: a ** 2

print(kvadratu(2))"""

"""sarasas = [2, 5, 6, 7, 8, 54, 87]

sarasas2 = map(lambda a: a ** 2, sarasas)

for skaicius in sarasas2:
    print(skaicius)"""

"""daugyba_is_saves = [lambda i=skaicius: i*i for skaicius in range(1, 6)]
for vienas in daugyba_is_saves:
    print(vienas))"""

"""keliamieji = [lambda i=metai: i for metai in range(1900, 2701) if
              (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)]
for vienas in keliamieji:
    print(vienas())"""