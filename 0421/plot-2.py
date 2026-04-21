import matplotlib.pyplot as plt

dataX = [100,200,300,400,500]
dataY = [10,20,50,60,30]

plt.plot(dataX,dataY,
         color='#0af',
         linestyle='-.',
         linewidth=1,
         marker='o',
         markersize=15,
         markerfacecolor='green',
         markeredgecolor='orange',
         markeredgewidth=4,
         )

plt.show()