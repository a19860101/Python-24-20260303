import pandas as pd

users = [
    {'name':'John','birth':'1990','gender':'m'},
    {'name':'Mary','birth':'1997','gender':'f'},
    {'name':'Kate','birth':'1999','gender':'f'},
    {'name':'Liam','birth':'1998','gender':'m'},
]
df = pd.DataFrame(users)

print(df)
# print(df.index)
# print(df.columns)
# print(df.shape)
# print(df.size)
