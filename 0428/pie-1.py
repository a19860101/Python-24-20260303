import matplotlib.pyplot as plt

data = [22,46,85,10]
label = ['A','B','C','D']
explode = (0,0.1,0,0)
colors = ['r','g','b','y']

plt.pie(data, labels=label, explode=explode, autopct='%1.1f%%',startangle=30, shadow=True, colors=colors)

plt.show()