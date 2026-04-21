import matplotlib.pyplot as plt
import pandas as pd

tsmc = pd.read_csv('./FMSRFK_2330_2025.csv',encoding='big5',header=1)

tsmc = tsmc.dropna(subset='月份')

# tsmc_max = tsmc['最高價'].astype('str').str.replace(',','').astype('float')
# tsmc_min = tsmc['最低價'].astype('str').str.replace(',','').astype('float')
# tsmc_ave = tsmc['加權(A/B)平均價'].astype('str').str.replace(',','').astype('float')
# plt.plot(range(1,13),tsmc_max)
# plt.plot(range(1,13),tsmc_min)
# plt.plot(range(1,13),tsmc_ave)


cols = ['最高價','最低價','加權(A/B)平均價','成交金額(A)']
for col in cols:
    tsmc[col] = tsmc[col].astype('str').str.replace(',','').astype('float')

plt.plot(range(1,13),tsmc['最高價'])
plt.plot(range(1,13),tsmc['最低價'])
plt.plot(range(1,13),tsmc['加權(A/B)平均價'])
plt.plot(range(1,13),tsmc['成交金額(A)'])


plt.show()

