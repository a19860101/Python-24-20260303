import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# tsmc = yf.download('2330.TW', period='1y')
#
# close = tsmc.get('Close')
# close.plot()
# plt.show()

tw0050 = yf.download('0050.TW',period='1y')

tw0050[['High','Low']].plot(figsize=(12,6),color=['red','blue'])
plt.title('0050')
plt.show()

