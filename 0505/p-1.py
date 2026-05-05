import requests

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

res = requests.get(url)

print(res.text)