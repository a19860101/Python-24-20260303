import pandas as pd

df1 = pd.read_json('./每日各站進出站人數-2026.json')

df2 = pd.read_json('./車站基本資料集.json')

print(df1)
print(df2)

result = pd.merge(df1, df2, left_on='staCode' ,right_on='stationCode')
print(result.iloc[30])
