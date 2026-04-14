import pandas as pd

df = pd.read_json('./TransService.json')


# 清除空格

# print(df['animal_Variety'].unique())
df['animal_Variety'] = df['animal_Variety'].astype('str').str.strip()
# print(df['animal_Variety'].unique())

# 統整資料

df['animal_Variety'] = df['animal_Variety'].replace({
    '混種犬':'混種狗',
    '玩具貴賓犬':'迷你貴賓犬',
    '': '未知品種'
})

print(df['animal_Variety'].unique())
print(df['animal_Variety'].nunique())

print(df['animal_Variety'].value_counts(ascending=True).head(10))