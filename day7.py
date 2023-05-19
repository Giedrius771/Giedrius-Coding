import os
import datetime

# Sukuriamas failas "Tekstas.txt" su pilnu tekstu "Zen of Python"
with open("Tekstas.txt", "w") as f:
    f.write("Zen of Python")

# Atspausdinamas tekstas iš sukurto failo
with open('Tekstas.txt', 'r') as f:
    print(f.read())

# Pridedama šiandienos data ir laikas paskutinėje failo eilutėje
with open('Tekstas.txt', 'a') as f:
    now = datetime.datetime.today()
    f.write('\n' + now.strftime("%Y-%m-%d %H:%M:%S"))

# Sunumeruojamos teksto eilutės
with open('Tekstas.txt', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    for i, line in enumerate(lines, 1):
        f.write(f'{i}. {line}')

# Pakeičiamas sakinys "Zen of Python" į "Gražu yra geriau nei bjauru."
with open('Tekstas.txt', 'r+') as f:
    text = f.read()
    text = text.replace("Zen of Python", "Gražu yra geriau nei bjauru.")
    f.seek(0)
    f.write(text)
    f.truncate()

# Atspausdinamas viso failo tekstas atbulai
with open('Tekstas.txt', 'r') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.rstrip()[::-1])

# Skaičiuojami žodžiai, skaičiai, didžiosios ir mažosios raidės failo tekste
with open('Tekstas.txt', 'r') as f:
    text = f.read()
    word_count = len(text.split())
    number_count = sum(char.isdigit() for char in text)
    uppercase_count = sum(char.isupper() for char in text)
    lowercase_count = sum(char.islower() for char in text)

print(f'Žodžių skaičius: {word_count}')
print(f'Skaičių skaičius: {number_count}')
print(f'Didžiųjų raidžių skaičius: {uppercase_count}')
print(f'Mažųjų raidžių skaičius: {lowercase_count}')