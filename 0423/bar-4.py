import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Microsoft Jhenghei')

data = pd.read_csv('./covid_jp.csv')

print(data)
w = 0.4
x = data.columns[2:-1]

y_jp_110 = data.iloc[3]['日本']
y_jp_114 = data.iloc[7]['日本']

y_dp_110 = 0
y_dp_114 = 0

y_ch_110 = data.iloc[3]['中國大陸']
y_ch_114 = data.iloc[7]['中國大陸']

y110 = [int(y_jp_110), int(y_dp_110), int(y_ch_110)]
y114 = [int(y_jp_114), int(y_dp_114), int(y_ch_114)]

plt.xticks(range(1,len(x)+1),x)
plt.bar([i for i in range(1,len(x)+1)], y110, align='edge',width=w)
plt.bar([i-w/2 for i in range(1,len(x)+1)], y114, width=w)

plt.show()
