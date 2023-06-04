# 1 uzduotis
import datetime

start_data = input("Iveskite pradzios data (pvz. 1998-04-05 04:51:12): ")
end_data = input("Iveskite pabaigos data (pvz. 1999-04-05 04:52:12): ")

start = datetime.datetime.strptime(start_data, "%Y-%m-%d %H:%M:%S")
end = datetime.datetime.strptime(end_data, "%Y-%m-%d %H:%M:%S")

skirtumas = end - start
skirtumas_sekundemis = skirtumas.total_seconds()

print(f"Pradzios data: {start}")
print(f"Pabaigos data: {end}")
print(f"Skirtumas tarp datu: {skirtumas}")
print(f"Skirtumas sekundemis: {skirtumas_sekundemis} s")
# 2 uzduotis
from datetime import datetime, timedelta

now = datetime.now()
print("Dabartine data ir laikas:", now)

five_days_ago = now - timedelta(days=5)
print("Data 5 dienas atgal:", five_days_ago)

eight_hours_later = now + timedelta(hours=8)
print("Data ir laikas 8 valandas po:", eight_hours_later)

formatted_now = now.strftime("%Y %m %d, %H:%M:%S")
print("Dabartinis laikas pagal reikalaujama formata:", formatted_now)
# 3 uzduotis
from datetime import datetime

# Leidzia vartojui parasyti tyksliai savo gimimo data ir nuo jos nuimti laika iki dabar
birthday_str = input("Iveskite savo gimtadieni (e.g. 2000-01-01 00:00:00): ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d %H:%M:%S")

# Suskaiciuoja ir atspausdina kiek praejo laiko nuo ivesto laiko
now = datetime.now()
elapsed_time = now - birthday

# Suskaiciuoja metus, dienas, valanda, minutes, ir sekundes
elapsed_days = elapsed_time.days
elapsed_seconds = elapsed_time.total_seconds()
elapsed_minutes = elapsed_seconds // 60
elapsed_hours = elapsed_minutes // 60
elapsed_months = elapsed_days // 30
elapsed_years = elapsed_days // 365

# Atspausdina rezultata
print(f"Praejas laikas {birthday_str}:")
print(f"{round(elapsed_years)} Metai")
print(f"{round(elapsed_months)} menesiai")
print(f"{round(elapsed_days)} dienos")
print(f"{round(elapsed_hours)} valandos")
print(f"{round(elapsed_seconds)} sekundes")
# 4 uzduotis
import datetime

try:
    start_data = input("Iveskite pradzios data (pvz. 1998-04-05 04:51:12): ")
    start = datetime.datetime.strptime(start_data, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Klaida: neteisinga pradzios data")
    exit()

try:
    end_data = input("Iveskite pabaigos data (pvz. 1999-04-05 04:52:12): ")
    end = datetime.datetime.strptime(end_data, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Klaida: neteisinga pabaigos data")
    exit()

skirtumas = end - start
skirtumas_sekundemis = skirtumas.total_seconds()

print(f"Pradzios data: {start}")
print(f"Pabaigos data: {end}")
print(f"Skirtumas tarp datu: {skirtumas}")
print(f"Skirtumas sekundemis: {skirtumas_sekundemis} s")
# 4- antra dalis
from datetime import datetime

try:
    # Leidzia vartojui parasyti tyksliai savo gimimo data
    birthday_str = input("Iveskite savo gimtadieni (e.g. 2000-01-01 00:00:00): ")
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d %H:%M:%S")

    # Suskaiciuoja ir atspapausdina kiek praejo laiko nuo ivesto laiko
    now = datetime.now()
    elapsed_time = now - birthday

    # Suskaiciuoja metus, dienas, valanda, minutes, ir secundes
    elapsed_days = elapsed_time.days
    elapsed_seconds = elapsed_time.total_seconds()
    elapsed_minutes = elapsed_seconds // 60
    elapsed_hours = elapsed_minutes // 60
    elapsed_months = elapsed_days // 30
    elapsed_years = elapsed_days // 365

# Atspausdina rezultata
    print(f"Praejas laikas {birthday_str}:")
    print(f"{elapsed_years} Metai")
    print(f"{elapsed_months} menesiai")
    print(f"{elapsed_days} dienos")
    print(f"{elapsed_hours} valandos")
    print(f"{elapsed_seconds} sekundes")
except ValueError:
    print("Ivestas blogas datos formatas. Formatas turi buti: YYYY-MM-DD HH:MM:SS")
except Exception as e:
    print(f"Ivyko klaida: {e}")

# 5 uzduotis
import datetime
import time

word = input("Iveskite zodi kuri norit kad kartotu: ")

while True:
    seconds = input("Iveskite sekundziu skaiciu kuri norite kad kartotu kiekviena atspausdinima: ")

    try:
        seconds = int(seconds)
    except ValueError:
        print("Neteisingai ivesta. Prasome ivesti skaiciu.")
        continue

    break

print(f"Spausdinama '{word}' kas {seconds} sekundes...")

while True:
    print(word)
    time.sleep(seconds)

### TAIP PRIDEDU KAD JEIGU REIKS ###
"""import datetime

def is_valid_personal_code(personal_code):
    # Check if the personal code has 11 digits
    if len(personal_code) != 11:
        return False

    # Check if the first six digits represent a valid birth date
    try:
        birth_date = datetime.datetime.strptime(personal_code[:6], '%y%m%d')
    except ValueError:
        return False

    # Check if the seventh digit represents a valid gender
    gender = int(personal_code[6])
    if gender not in [1, 2, 3, 4, 5, 6, 7, 8]:
        return False

    # Check if the checksum is correct
    checksum = int(personal_code[10])
    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    digits = [int(d) for d in personal_code[:-1]]
    total = sum([f * d for f, d in zip(factors, digits)]) % 11
    if total == 10:
        total = sum([f * d for f, d in zip(factors, digits)]) % 10
    if total != checksum:
        return False

    # If all checks passed, the personal code is valid
    return True

personal_code = input("Enter personal code: ")
print(is_valid_personal_code(personal_code))
"""

def is_valid_personal_code(personal_code):
    if not personal_code.isdigit() or len(personal_code) != 11:
        return False

    gender = int(personal_code[6])
    if gender not in [1, 2, 3, 4, 5, 6, 7, 8]:
        return False

    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    digits = list(map(int, personal_code))
    total = sum([f * d for f, d in zip(factors, digits)]) % 11 % 10
    return total == digits[-1]

personal_code = input("Enter personal code: ")
print(is_valid_personal_code(personal_code))


def skaiciuoti_zodziu_savybes(self):
    num_words = len(self.text.split())
    num_digits = sum(1 for char in self.text if char.isdigit())
    num_uppercase = sum(1 for char in self.text if char.isupper())
    num_lowercase = sum(1 for char in self.text if char.islower())
    return {num_words}, [num_digits], {num_uppercase}, {num_lowercase}

kintamasis2 = Sakinys("Siandien yra penktadienis 2023")
print(f"Number of words: {num_words}")
print(f"Number of digits: {num_digits}")
print(f"Number of uppercase letters: {num_uppercase}")
print(f"Number of lowercase letters: {num_lowercase}")