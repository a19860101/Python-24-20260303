import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
heights = np.random.normal(165,10,100)
print(heights)
bmi = np.random.normal(21,2,100)
print(bmi)
# bmi 體重/身高平方
weights = bmi * ((heights/100) ** 2)
print(weights)

# plt.scatter(heights,weights)
plt.scatter(weights,heights)
plt.show()
