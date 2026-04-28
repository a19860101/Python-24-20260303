import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./mobile_os.csv')

result = data.iloc[12].tolist()
result = result[1:]
print(data)
print(result)

label = data.columns[1:]
print(label)
explode = [0,0.05,0,0]

plt.pie(result, labels=label, explode=explode)

plt.show()