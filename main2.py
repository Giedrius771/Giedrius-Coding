# uzduotis1
sarasas.append(5)
print(sarasas)
sarasas.append("stalas")
print(sarasas)

sarasas = ["Laba diena"]
sarasas.append("stalas")
print(sarasas)

sarasas = ["Laba diena", "stalas"]
sarasas.remove("stalas")
print(sarasas)

sarasas = ["Labas vakaras"]
sarasas.insert(1, "Diena")
print(sarasas)

sarasas = ["Laba diena", "stalas", "vakariene", "kava"]

index = sarasas.index("stalas")
print("Index of 'stalas':", index)

print("Element at index 2:", sarasas[2])

sarasas[1] = "lentyna"
print("New list with 'lentyna':", sarasas)


# uzduotis 2

prompt = "enter a number: "
summ = 0
a = int(input(prompt))
while a >= 0:
    summ = summ + a
    a = int(input(prompt))
print(summ)


# uzduotis 3

zodziu_sarasas = []
for zodziai in range(5):
  zodziai = str(input("Iveskite 5 zodzius:"))
  zodziu_sarasas.append(zodziai)

index = 1
for element in zodziu_sarasas:
  print("Zodis:", element, "Ilgis", len(element), "Indeksas", index)
  index += 1

# 4 uzduotis
import random

count = 0

while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Laimejai")
        break
    count += 1
else:
    print("Pralaimejai")
# 5 uzduotis
start_year = int(input("Iveskite prasidedancius metus: "))
end_year = int(input("Iveskite pasibaigiancius metus: "))
moving_years = []
non_moving_years = []
for year in range(start_year, end_year + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        moving_years.append(year)
    else:
        non_moving_years.append(year)
choice = input("Kuriuos metus nori kad rodytu? Enter 'keliamieji' or 'nekeliamieji': ")
if choice == "keliamieji":
    print("keliamieji metai:")
    for year in moving_years:
        print(year)
elif choice == "nekeliamieji":
    print("nekeliamieji:")
    for year in non_moving_years:
        print(year)
else:
    print("Blogas pasirinkimas. Iveskite 'keliamieji' or 'nekeliamieji'.")
leap_years = []

for year in range(1900, 2101):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)
print("Leap years from 1900 to 2100:")
for year in leap_years:
    print(year)