import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
data = pd.read_csv('./NPA_TD1.csv', header=1)

# 總數量
total = len(data)
print(total)
# 國道一號數量
ta = '國道一號'
condition = data['設置縣市'] == ta
s1 = len(data[condition])
print(s1)

# 國道一號數量
ta3 = '國道三號'
condition3 = data['設置縣市'] == ta3
s3 = len(data[condition])
print(s3)

other = total - s1 - s3


plt.pie([s1, other,s3],labels=[ta,'其他', ta3], autopct='%1.1f%%', explode=[0.2,0,0.2])
plt.title('國道一號三號測速執法點比例')
plt.show()