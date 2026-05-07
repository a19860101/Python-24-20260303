import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tsmc = yf.download('2330.TW', period='1y')

close = tsmc.get('Close')

close.plot()

plt.show()