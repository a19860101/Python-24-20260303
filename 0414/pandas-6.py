import pandas as pd

df = pd.read_json('./TransService.json')

print(df['animal_Variety'].unique())
df['animal_Variety'] = df['animal_Variety'].astype('str').str.strip()
print(df['animal_Variety'].unique())