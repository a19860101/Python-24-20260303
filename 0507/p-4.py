import yfinance as yf

tsmc = yf.Ticker('2330.TW')
apple = yf.Ticker('AAPL')


# print(tsmc.history('1d').columns)
# print(tsmc.history('7d')['Close'])
# print(tsmc.history('6mo')['Close'])
# print(tsmc.history('1y')['Close'])

# print(tsmc.history(period="max")['Close'])

tsmc_info = tsmc.info
print(tsmc_info)
print(tsmc_info.get('currentPrice'))