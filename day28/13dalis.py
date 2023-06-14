import pandas as pd
import csv
import numpy as np

csv_file_path = 'miestai_isvalyti.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)

df = pd.read_csv(csv_file_path)
df = pd.read_csv(csv_file_path, index_col='Miestas')

cities = df[df['1897'] > df['2019']].index

print(cities)
