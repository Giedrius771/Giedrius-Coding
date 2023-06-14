import pandas as pd
import csv
import numpy as np

df = pd.read_csv('miestai_isvalyti.csv', index_col='Miestas')

df['Pokytis'] = ((df['2019'] - df['1989']) / df['1989']) * 100

didziausias_padidejimas = df.sort_values('Pokytis', ascending=False).head(1)
didziausias_sumazejimas = df.sort_values('Pokytis').head(1)

print("Labiausiai procentaliai padidėjęs miestas nuo 1989 m.:")
print(didziausias_padidejimas[['2019', '1989', 'Pokytis']])
print("\nLabiausiai procentaliai sumažėjęs miestas nuo 1989 m.:")
print(didziausias_sumazejimas[['2019', '1989', 'Pokytis']])
