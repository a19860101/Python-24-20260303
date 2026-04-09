import pandas as pd

datas = pd.read_json('./每日各站進出站人數-2026.json')
datas.columns = ['乘車日','車站代碼','進站人數','出戰人數']
print(datas)