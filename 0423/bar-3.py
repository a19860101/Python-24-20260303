import matplotlib.pyplot as plt

x = ['A','B','C','D']

y1 = [100,120,80,60]
y2 = [150,60,120,200]

plt.xticks(range(1,5), x)


plt.bar([1,2,3,4], y1, width=0.4, align='edge')
plt.bar([.8,1.8,2.8,3.8], y2,width=0.4)

plt.show()
