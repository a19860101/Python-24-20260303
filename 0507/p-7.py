import yfinance as yf
import mplfinance as mpf
from pygments.lexer import inherit

tsmc = yf.Ticker('00899.TW')
data = tsmc.history(period="6mo")

# mpf.plot(data, type='candle')
mc = mpf.make_marketcolors(
    up='red',
    down='green',
    edge='inherit',
    # volume='in',
    inherit=True,
)
s = mpf.make_mpf_style(
    base_mpf_style='nightclouds',
    marketcolors=mc,
    gridstyle='--'
)

mpf.plot(data,type='candle',style=s,volume=True,mav=(5,20))
