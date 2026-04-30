import pandas as pd

data = pd.read_csv('./NPA_TD1.csv', header=1)

# condition = data['設置縣市'].str.contains('北')
condition = data['設置縣市'] == '臺北市'
print(data[condition])

# print(data['設置縣市'].value_counts())
q = data['設置縣市'].value_counts()
print(q)
n = []
for i in q:
    n.append(i)

print(n)
