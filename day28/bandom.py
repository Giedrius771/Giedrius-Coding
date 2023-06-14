import pandas as pd
import numpy as np
import csv

csv_file_path = 'miestai_isvalyti.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    df = pd.read_csv(csv_file_path, index_col='Miestas')

    for row in csv_reader:
        print(row)

print(df.head(5))

gyventojai = df[['Marijampolė', '2019']]
print(gyventojai)
##### 6 dalis #####
stulpelis_1897 = df['1897'].head(5)
print(stulpelis_1897)
### 7 ###
stulpeliai = df[['2019', '1970', '1923']].head(10)
print(stulpeliai)
##### 8 ####
eiluciu_skaicius = df.shape[0]
print(f"Lenteleje yra {eiluciu_skaicius} eiluciu.")
#### 9 #####
df['Numeracija'] = df.reset_index().index + 1
print(df)
###### 10 #####
nuoiki = df.iloc[30:40]
print(nuoiki)
#### 11 ###
df = df.drop('Numeracija', axis=1)
##### 12 #####
missing_1959 = df[df['1959'].isnull()]['Miestas']
print(missing_1959)
##### 13 ####
miestai = df[df['1897'] > df['2019']]['Miestas']
print(miestai)
