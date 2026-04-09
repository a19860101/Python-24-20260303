import pandas as pd

from datetime import datetime

users = [
    {'name':'John','birth':'1990','gender':'m'},
    {'name':'Mary','birth':'1997','gender':'f'},
    {'name':'Kate','birth':'1999','gender':'f'},
    {'name':'Liam','birth':'2006','gender':'m'},
]
df = pd.DataFrame(users,index=['A','B','C','D'],columns=['name','birth','gender'])
# df.columns = ['姓名','出生年份','性別']
print(df)
# print(df.index)
# print(df.columns)
# print(df.shape)
# print(df.size)

# 求目前年齡
current_year = datetime.today().year
# print(current_year)

df['age'] = current_year - df['birth'].astype(int)
# print(df)

# 數學計算
print(df['age'])
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())
print(df['age'].median())
print(df['age'].std())
print(df['age'].describe())

# print(df['name'])
# print(df['gender'])
# print(df.loc['A'])
# print(df.iloc[0])
# print(df.loc[1])

# 條件篩選
# condition = df['age'] >= 25
# condition = df['name'] == 'Mary'
# condition = df['name'] == 'QQ'

condition = df['name'].str.contains('A&a')
# condition = df['name'].str.contains('A|a')

print(df[condition])

