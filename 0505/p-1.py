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