import re


# 1 uzduotis###
def keisti_data(data):
    regex = r"(\d{2})\.(\d{2})\.(\d{4})"
    match = re.search(regex, data)
    if match:
        rezultatas = f"{match.group(3)} {match.group(2)} {match.group(1)}"
    else:
        regex_fix = r"(\d{4})\.(\d{2})\.(\d{2})"
        match_fix = re.search(regex_fix, data)
        if match_fix:
            rezultatas = f"{match_fix.group(1)} {match_fix.group(2)} {match_fix.group(3)}"
        else:
            rezultatas = "Invalid date format"
    return rezultatas


print(keisti_data("25.05.2023"))
print(keisti_data("01.12.2022"))
print(keisti_data("2022.23.05"))
##### 2 uzduotis ###
# import re
#
# text = '''Workshop & Tutorial proposals: November 21, 2019
# Notification of acceptance: December 1, 2019
# Workshop & Tutorial websites online: December 18, 2019
# Workshop papers: February 28, 2020
# Workshop paper notifications: March 27, 2020
# Workshop paper camera-ready versions: April 10, 2020
# Tutorial material due (online): April 10, 2020'''
#
# date_regex = r"([A-Za-z]+\s\d{1,2},\s\d{4})"
#
# date_list = re.findall(date_regex, text)
#
# print(date_list)
## 3 uzduotis####
import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

event_date_regex = r"([^:]+):\s([A-Za-z]+\s\d{1,2},\s\d{4})"

event_date_list = re.findall(event_date_regex, text)

for i, (event, date) in enumerate(event_date_list, 1):
    print(f"\n# {i}.")
    print(f"Event: {event.strip()}")
    print(f"Date: {date.strip()}")

########## 4 uzduotis ####
import re


def cenzura(tekstas, *keiksmai):
    for keiksma in keiksmai:
        cenzuruoti_zodziai = re.findall(r'\b' + re.escape(keiksma) + r'\b', tekstas)
        for zodis in cenzuruoti_zodziai:
            cenzuruotas_zodis = zodis[0] + '*' * (len(zodis) - 2) + zodis[-1]
            tekstas = tekstas.replace(zodis, cenzuruotas_zodis)
    return tekstas


# Pavyzdinis iškvietimas:
tekstas = 'Baisūs žodžiai, tokie kaip kvaraba, žaltys, ciuciundra ,kutvela'
cenzuruotas_tekstas = cenzura(tekstas, 'kvaraba', 'žaltys', 'ciuciundra', 'kutvela')
print(cenzuruotas_tekstas)
########### 2 budas 4 su pattern
import re


def cenzura(tekstas, *keiksmai):
    for keiksma in keiksmai:
        pattern = r'\b' + re.escape(keiksma) + r'\b'
        tekstas = re.sub(pattern,
                         lambda match: match.group(0)[0] + '*' * (len(match.group(0)) - 2) + match.group(0)[-1],
                         tekstas, flags=re.IGNORECASE)
    return tekstas


tekstas = 'Baisūs žodžiai, tokie kaip kvaraba, žaltys, ciuciundra, kutvela'
cenzuruotas_tekstas = cenzura(tekstas, 'kvaraba', 'žaltys', 'ciuciundra', 'kutvela')

groups = re.split(r',\s*', cenzuruotas_tekstas)
print(groups)
