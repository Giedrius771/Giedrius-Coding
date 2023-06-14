import pandas as pd
import csv

csv_file_path = 'miestai_isvalyti.csv'

df = pd.read_csv(csv_file_path, index_col='Miestas')

missing_1959 = df[df['1959'] == 0]
print("Cities that had no population in 1959:")
print(missing_1959.to_string())
