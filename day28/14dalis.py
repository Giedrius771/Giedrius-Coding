import pandas as pd
import csv

csv_file_path = 'miestai_isvalyti.csv'

df = pd.read_csv(csv_file_path, index_col='Miestas')
increased_population_cities = df[df['2019'] > df['2011']]

increased_population_cities = increased_population_cities[['2019', '2011']]
print(increased_population_cities)
