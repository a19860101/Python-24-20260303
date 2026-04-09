import pandas as pd

datas = pd.read_json('./每日各站進出站人數-2026.json')

# datas.columns = ['乘車日','車站代碼','進站人數','出戰人數']
# print(datas['trnOpDate'])
# 216
# condition = datas['trnOpDate'] == 20260216
# print(datas[condition]['gateInComingCnt'].max())

# datas216 = datas[condition] #216進站人數

# datas216_max = datas216['gateInComingCnt'].idxmax()

# print(datas216.loc[datas216_max])

# taipei = datas[datas['staCode']==1000]
# taipei_max = taipei['gateInComingCnt'].idxmax()
# print(taipei.loc[taipei_max])

# 取得20260101當日最少進站人數
condition = datas['trnOpDate'] == 20260101
datas0101 = datas[condition]
datas0101_min = datas0101['gateInComingCnt'].idxmin()
print(datas0101.loc[datas0101_min])




