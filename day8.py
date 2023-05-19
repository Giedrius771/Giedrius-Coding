#1 uzduotis
tekstas = "Laba diena siandien yra treciadienis"
tekstas2 = "Kaip noreciau kad jau butu penktadienis"

tekstasnew = " ".join(tekstas.split()) + "!"
pasirinktas = " ".join([tekstas] + tekstas2.split()) + "!"

print(tekstasnew)
print(pasirinktas)
## 2 uzduotis#############
from statistics import mean, median


sarasas = list(range(0, 50))  # Modifying the range to exclude 0

daugyba = [sk * 10 for sk in sarasas]
print(daugyba)

dalyba = list(filter(lambda sk: sk % 7 == 0, sarasas))
print(dalyba)

kvadratu = [sk ** 2 for sk in sarasas]
print(kvadratu)

suma = sum(kvadratu)
maziausias = min(kvadratu)
didziausias = max(kvadratu)
vidurkis = mean(kvadratu)
mediana = median(kvadratu)

print("Suma:", suma)
print("Mažiausias skaičius:", maziausias)
print("Didžiausias skaičius:", didziausias)
print("Vidurkis:", vidurkis)
print("Mediana:", mediana)


atbulai = sorted(kvadratu, reverse=True)
print(atbulai)
#### 3 uzduotis#################################
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

def skaiciu_suma(sarasas):
    suma_skaiciu = 0
    for x in sarasas:
        if isinstance(x, (int, float)):
            if not isinstance(x, bool):  # Exclude boolean values
                suma_skaiciu += x
    return suma_skaiciu

def spausdinti_zodzius(sarasas):
    zodziai = [str(x) for x in sarasas if isinstance(x, str)]
    sujungti_zodziai = " ".join(zodziai)
    print("Visi žodžiai:", sujungti_zodziai)

def skaiciuoti_true(sarasas):
    kiek_true = sum([1 for x in sarasas if isinstance(x, bool) and x is True])
    print("Kiek sąraše yra True reikšmių:", kiek_true)

print("Visų skaičių suma:", skaiciu_suma(sarasas))
spausdinti_zodzius(sarasas)
skaiciuoti_true(sarasas)

### 4 uzduotis
from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f"{self.vardas} {self.amzius}"

z1 = Zmogus("Brigita", 25)
z2 = Zmogus("Giedrius", 30)
z3 = Zmogus("Henrikas", 20)
z4 = Zmogus("Danielius", 44)
z5 = Zmogus("Egidijus", 19)
z6 = Zmogus("Algirdas", 56)

zmogus_list = [z1, z2, z3, z4, z5, z6]

sorted_by_name = sorted(zmogus_list, key=attrgetter('vardas'))
print("Sorted by name:", sorted_by_name)

reversed_sorted_by_name = list(reversed(sorted_by_name))
print("Reversed sorted by name:", reversed_sorted_by_name)

sorted_by_age = sorted(zmogus_list, key=attrgetter('amzius'))
print("Sorted by age:", sorted_by_age)

reversed_sorted_by_age = list(reversed(sorted_by_age))
print("Reversed sorted by age:", reversed_sorted_by_age)