import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
data = pd.read_csv('./NPA_TD1.csv', header=1)

# condition = data['設置縣市'].str.contains('北')
condition = data['設置縣市'] == '臺北市'
# print(data[condition])

# print(data['設置縣市'].value_counts())
q = data['設置縣市'].value_counts()

# print(q.values)
# print(q.index)
q_v = q.values.tolist()
q_i = q.index.tolist()

print(q_v)
print(q_i)

# 最多的
q_max = q_v[0]
# print(q_v[0])
# print(max(q_v))
# print(q_i[0])
q_other = sum(q_v) - q_max



# plt.bar(q_i, q_v)
# plt.pie(q_v)
plt.pie([q_max, q_other],labels=[q_i[0],'其他'], autopct='%1.1f%%', explode=[0.08,0])
plt.title('新北市測速執法點比例')
plt.show()