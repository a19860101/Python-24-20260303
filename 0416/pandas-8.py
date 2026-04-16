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
#
# r = result.dropna(axis=1,how='all')
# print(r.columns)

# r2 = result.dropna(axis=0,subset=['Region'])
# print(r2)

# NaN,None,NaT

# axis：往哪邊砍？（0砍列，1砍欄）
# subset：砍哪一區？（指定哪幾個欄位）
# how：砍多兇？（看到一個就砍，還是全空才砍）

fill_region = empty_region.fillna('區域未知')

print(fill_region['Region'])