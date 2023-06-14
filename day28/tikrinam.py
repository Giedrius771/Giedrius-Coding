import pandas as pd
import csv

csv_failas = 'miestai_isvalyti.csv'

df = pd.read_csv(csv_failas, index_col='Miestas')

missing_1959 = df[df['1959'].isnull()]['Miestas']
print(missing_1959)
