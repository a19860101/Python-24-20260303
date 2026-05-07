import yfinance as yf
import mplfinance as mpf

tsmc = yf.Ticker('2330.TW')
data = tsmc.history(period="3mo")

mpf.plot(data, type='candle')
