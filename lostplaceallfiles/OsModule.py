import os

curDir = os.getcwd()
print(curDir)

print(os.listdir())

os.mkdir('NewDir')

import time

time.sleep(2)

os.rename('newDir','newDir2')
time.sleep(2)

os.rmdir('newDir2')

os.chdir()

"""os.makedirs("Naujas/Naujausias/Geras", exist_ok=True)"""
failas = open("failas.txt", 'w')
failas.write("Sveiki visi!")
failas.close()
print(failas.read())

with open("failas.txt", 'r') as failas:
    print(failas.read()) ## geriausias metodas

with open("failas.txt", 'r', encoding="utc-8") as failas:
    print(failas.read()) ## geriausias metodas

    with open("Tekstas.txt", "w") as w_failas:
        w_failas.write("Zen of Python")
    with open("Tekstas.txt", "r") as r_failas:
        print(r_failas.read())
    with open("Tekstas.txt", "w") as w_failas:
        w_failas.write("Zen of Python\n")
        dabartine_data = datetime.datetime.now()
        str_data = dabartine_data.strftime("%Y %m %d %H:%M:%S")
        w_failas.write(str_data)