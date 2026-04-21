import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

dataX = ['日','Mon','Tue','Wed','Thu','Fri','Sat']
dataY = [28,30,24,10,35,40,16]

plt.ylim(0,60)
# plt.xlim()

plt.yticks(range(0,60,5))
# plt.xticks(range(0,60,5))

plt.plot(dataX,dataY,label='天氣')
plt.legend()
plt.show()
