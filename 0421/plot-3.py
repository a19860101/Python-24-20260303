import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

dataX = ['日','Mon','Tue','Wed','Thu','Fri','Sat']
dataY = [28,30,24,10,35,40,16]
dataY2 = [18,20,14,20,25,30,36]

plt.ylim(0,60)
# plt.xlim()

plt.yticks(range(0,60,5))
# plt.xticks(range(0,60,5))

plt.title('weather')
plt.xlabel('星期')
plt.ylabel('溫度(攝氏)')
plt.grid()

plt.plot(dataX,dataY,label='台北一周天氣',marker='o')
plt.plot(dataX,dataY2,label='東京一周天氣',marker='o')

plt.legend()
plt.show()
