import pandas as pd

csv_file_path = 'miestai_isvalyti.csv'

df = pd.read_csv(csv_file_path).reset_index(drop=True)

print(df)

df.to_csv('output.csv', index=False)
