import pandas as pd
import json

# with open('./restaurant_C_f.json', 'r', encoding='utf-8-sig') as f:
#     json_data = json.load(f)
#
#
# data = pd.DataFrame(json_data)
#
# print(data)

data = pd.read_csv('./Restaurant_C_f.csv')

print(data)