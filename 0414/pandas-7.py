import pandas as pd
import json

with open('./restaurant_C_f.json', 'r', encoding='utf-8-sig') as f:
    json_data = json.load(f)


data = pd.DataFrame(json_data['XML_Head']['Infos']['Info'])

# print(data.iloc[0])
# print(data.columns)

condition = data['Add'].str.contains('新北市220板橋區')
print(data[condition]['Name'])

# data = pd.read_csv('./Restaurant_C_f.csv')
# print(data)