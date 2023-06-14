### 5 dalis ###
import pandas as pd
import csv
import numpy as np

csv_failas = 'miestai_isvalyti.csv'

with open(csv_failas, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        year = row[0]
        city = row[1]
        population = row[2]

        if year == '1923' and city == "Marijampolė":
            print(f"Zmoniu skaicius Marijampoleje 2019 buvo {population}.")
            break

df = pd.read_csv(csv_failas, index_col="Miestas")

gyventojai = df.loc['Marijampolė', '1923']
print(f"Zmoniu Marijampoleja 2019 buvo {gyventojai}")
###### 6 #####
stulpelis_1897 = df['1897'].head(5)
