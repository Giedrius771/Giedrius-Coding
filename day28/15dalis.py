import pandas as pd
import csv
import numpy as np

csv_file_path = 'miestai_isvalyti.csv'
df = pd.read_csv(csv_file_path, index_col='Miestas')

decreasing_population_cities = df[(df.loc[:, '1897':'2019'].diff(axis=1) <= 0).all(axis=1)]
print(decreasing_population_cities.loc[:, ['2019', '2011', '2001', '1989', '1979', '1970', '1959', '1923', '1897']])
