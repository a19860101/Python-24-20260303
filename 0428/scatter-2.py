import matplotlib.pyplot as plt
import numpy as np

np.random.seed(23)

# 單位:千元
x = np.random.uniform(10,100,100)

y = 30 + (x * 1.5) + np.random.normal(0,30,100)

x = np.append(x, [15])
y = np.append(y,[220])

x = np.append(x,[92])
y = np.append(y,[15])

plt.scatter(x,y)
plt.grid()
plt.show()