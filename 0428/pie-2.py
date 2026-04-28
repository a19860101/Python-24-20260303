import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./mobile_os.csv')

# result = data.iloc[12].tolist()
# result = result[1:]
# print(data)
# print(result)
#
# label = data.columns[1:]
# print(label)
# explode = [0,0.05,0,0]
#
# plt.pie(result, labels=label, explode=explode)
#
# plt.show()

print(data)

ios = data['iOS'].mean().round(2)
android = data['Android'].mean().round(2)
samsung = data['Samsung'].mean().round(2)
other = data['Other'].mean().round(2)

label = data.columns[1:]
explode = [0,0.05,0,0]
os_data = [ios, android, samsung, other]

print(os_data)
plt.pie(os_data, labels=label, explode=explode)
#
plt.show()
