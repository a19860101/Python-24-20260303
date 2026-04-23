import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

x = ['A','B','C']
y = [106,148,95]

# 垂直
plt.ylim(0,500)
plt.yticks(range(0,500,50))
plt.grid()
plt.xlabel('分類')
plt.ylabel('數量')
plt.title('垂直長條圖')
plt.legend()
result = plt.bar(x, y, label="數量" , color=['pink','orange','skyblue'], alpha=1, width=0.5, align='center')
plt.bar_label(result, color='red', fontsize=30)

# 水平
# plt.xlim(0,500)
# plt.xticks(range(0,500,50))
# plt.ylabel('分類')
# plt.xlabel('數量')
# plt.title('水平長條圖')
# plt.barh(x,y,label="數量")
# plt.legend()


plt.show()