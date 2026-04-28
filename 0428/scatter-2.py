import matplotlib.pyplot as plt
import numpy as np

np.random.seed(23)

# 單位:千元
x = np.random.uniform(10,100,100)

# 銷售數量
y = 30 + (x * 1.5) + np.random.normal(0,30,100)

# 狀況A：投放少賣很好
x = np.append(x, [15])
y = np.append(y,[220])

# 狀況B：投放多賣不好
x = np.append(x,[92])
y = np.append(y,[15])

plt.scatter(x,y)
plt.grid()
plt.show()