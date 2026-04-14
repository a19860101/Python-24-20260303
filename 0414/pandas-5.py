import pandas as pd

df = pd.read_json('./TransService.json')
# animal_kind
print(df['animal_Variety'])