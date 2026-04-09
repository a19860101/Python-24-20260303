import pandas as pd

from datetime import datetime

users = [
    {'name':'John','birth':'1990','gender':'m'},
    {'name':'Mary','birth':'1997','gender':'f'},
    {'name':'Kate','birth':'1999','gender':'f'},
    {'name':'Liam','birth':'2022','gender':'m'},
]
df = pd.DataFrame(users,index=['A','B','C','D'],columns=['name','birth','gender'])
# df.columns = ['姓名','出生年份','性別']
print(df)
# print(df.index)
# print(df.columns)
# print(df.shape)
# print(df.size)

current_year = datetime.today().year
print(current_year)

df['age'] = current_year - df['birth'].astype(int)
print(df)


# print(df['name'])
# print(df['gender'])
# print(df.loc['A'])
# print(df.iloc[0])
# print(df.loc[1])


