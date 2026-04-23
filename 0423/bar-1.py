import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

x = ['A','B','C']
y = [100,150,80]
# plt.ylim(0,500)
# plt.yticks(range(0,500,50))

plt.xlim(0,500)
plt.xticks(range(0,500,50))

plt.grid()
plt.xlabel('分類')
plt.ylabel('數量')
plt.title('圖')

# plt.bar(x, y, label="數量")
plt.barh(x,y)
plt.legend()

plt.show()