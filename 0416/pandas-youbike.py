import pandas as pd

# sarea 行政區
# available_rent_bikes 可借數量
# ar 地址
# sna 站點名稱

result = pd.read_json('https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json')[['sarea','sna','ar','available_rent_bikes']]

condition = (result['sarea'].str.contains('大安區')) & (result['available_rent_bikes'] > 5)

result = result[condition]

result['sna'] = result['sna'].str.replace('YouBike2.0_', '')
result.columns = ['行政區','站點名稱','地址','可借數量']
print(result)

result.to_excel('YouBike2.xlsx')
