import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='Microsoft Jhenghei')

data = pd.read_csv('./出國旅客按目的地統計.csv')

print(data)

x = data.columns[1:-1]
y = data.iloc[1][1:-1].astype('int')

plt.bar(x, y)

plt.show()