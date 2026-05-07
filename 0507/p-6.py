# 移動平均線是將過去某一段時間內的收盤價相加，再除以該天數所得出的平均值。
# 隨著時間推移，新的價格加入，舊的價格被剔除，這些平均點連成一條線，就是「移動」平均線。
#
# 舉例說明：
# 如果你想算 5 日均線（5MA），就是把過去 5 天的收盤價加起來除以 5。
# 到了明天，就用明天的收盤價替換掉 5 天前的那一個，重新計算。


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tw0050 = yf.download('0050.TW',period='3mo')

print(tw0050['Close'].rolling(window=20).mean())
tw0050['MA20'] = tw0050['Close'].rolling(window=20).mean()
tw0050['MA60'] = tw0050['Close'].rolling(window=60).mean()

tw0050[['Close','MA20','MA60']].plot(figsize=(12,4))
plt.show()

