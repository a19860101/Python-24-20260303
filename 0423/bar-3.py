import matplotlib.pyplot as plt

x = ['A','B','C','D','E','F']

# print(len(x))
# print(range(1,5))
# range(1,len(x)+1)

# w = 0.3
# print([i for i in range(1,len(x)+1)])
# print([i-w/2 for i in range(1,len(x)+1)])



y1 = [100,120,80,60,66,77]
y2 = [150,60,120,200,88,99]

plt.xticks(range(1,len(x)+1), x)


# plt.bar([1,2,3,4], y1, width=0.4, align='edge')
# plt.bar([.8,1.8,2.8,3.8], y2,width=0.4)

w = 0.2
plt.bar([i for i in range(1,len(x)+1)], y1,width=w, align='edge')
plt.bar([i-w/2 for i in range(1,len(x)+1)], y2,width=w, align='center')

plt.show()

