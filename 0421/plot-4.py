import matplotlib.pyplot as plt
import pandas as pd

tsmc = pd.read_csv('./FMSRFK_2330_2025.csv',encoding='big5',header=1)

# print(tsmc)
# print(tsmc['最高價'])

dataMAX = tsmc['最高價'].dropna().tolist()
dataMIN = tsmc['最低價'].dropna().tolist()

print(dataMAX)
print(dataMIN)

x = range(1,13)

plt.plot(x, dataMAX)

plt.show()