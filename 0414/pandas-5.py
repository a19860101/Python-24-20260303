import pandas as pd

df = pd.read_json('./TransService.json')
# animal_kind
# print(df['animal_Variety'])

# condition = df['animal_kind'].str.contains('蛇')
# print(df[condition])

# animal_types = df['animal_kind'].unique()
# animal_types = df['animal_Variety'].unique()
area = df['shelter_name'].unique()

# kind_count = df['shelter_name'].value_counts()
# print(kind_count)