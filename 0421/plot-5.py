import matplotlib.pyplot as plt
import pandas as pd

tsmc = pd.read_csv('./FMSRFK_2330_2025.csv',encoding='big5',header=1)

tsmc = tsmc.dropna(subset='月份')
print(tsmc.columns)
ave = tsmc['加權(A/B)平均價']

x = tsmc['月份']

print(ave)
ave_float = [float(d.replace(',','')) for d in ave]


dataMAX = tsmc['最高價']
dataMIN = tsmc['最低價']

dataMAX_float = [float(d.replace(',','')) for d in dataMAX]
dataMIN_float = [float(d.replace(',','')) for d in dataMIN]
print(ave_float)
print(dataMAX_float)
print(dataMIN_float)

plt.xticks(range(1,13))

plt.ylim(500,2000)
plt.yticks(range(500,2000,100))
plt.grid()
plt.plot(x, ave_float, marker='o', linestyle='-', color='red')
plt.fill_between(x, dataMAX_float, dataMIN_float,alpha=0.5,color='pink')

plt.show()