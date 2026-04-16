import pandas as pd

result = pd.read_csv('./Restaurant_C_f.csv')

print(result)
# print(result.columns)
# print(result['Name'].isnull())
# print(result['Name'].isnull().sum())
# print(result['Add'].isnull().sum())
# print(result['Region'].isnull().sum())

condition = result['Region'].isnull()
empty_region = result[condition]
print(empty_region)

# print(result.isnull().sum())

r = result.dropna(axis=1)
print(r.columns)

r2 = result.dropna(axis=0,subset=['Region'])
print(r2)
