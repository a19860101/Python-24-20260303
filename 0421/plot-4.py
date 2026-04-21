import matplotlib.pyplot as plt
import pandas as pd

tsmc = pd.read_csv('./FMSRFK_2330_2025.csv',encoding='big5',header=1)

print(tsmc.columns)
# print(tsmc['最高價'])

dataMAX = tsmc['最高價'].dropna().tolist()
dataMIN = tsmc['最低價'].dropna().tolist()

dataMAX_float = [float(d.replace(',','')) for d in dataMAX]
dataMIN_float = [float(d.replace(',','')) for d in dataMIN]

print(dataMAX)
print(dataMIN)
print(dataMAX_float)

x = range(1,13)

# plt.xlim(0,13)
plt.xticks(range(1,13))

plt.ylim(500,2000)
plt.yticks(range(500,2000,100))
plt.grid()

plt.plot(x, dataMAX_float, marker='o')
plt.plot(x, dataMIN_float, marker='o')
plt.fill_between(x, dataMAX_float, dataMIN_float,alpha=1,color='pink')

plt.show()