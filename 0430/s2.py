import pandas as pd

data = pd.read_csv('./NPA_TD1.csv', header=1)

# condition = data['設置縣市'].str.contains('北')
condition = data['設置縣市'] == '臺北市'
print(data[condition])