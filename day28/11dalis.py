import pandas as pd
import csv

csv_failas = 'miestai_isvalyti.csv'

df = pd.read_csv(csv_failas, index_col='Miestas')

print(df.to_string())
