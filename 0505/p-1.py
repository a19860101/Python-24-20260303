import bs4
import requests

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

res = requests.get(url)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

# print(htmlfile)
# print(htmlfile.find('h1').text)
# print(htmlfile.find('p'))
# print(htmlfile.find('p',class_='text-info').text)
title = htmlfile.find('h1').text

# print(title)
print(title.strip())

# print(htmlfile.select_one('tbody tr td:nth-of-type(3)'))
exc = htmlfile.select('tbody tr td:nth-of-type(3)')
for e in exc:
    print(e.text)

exc2 = htmlfile.select('tbody tr td:nth-of-type(5)')
for e in exc2:
    print(e.text.strip())