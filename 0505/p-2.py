import requests
import bs4
from setuptools.namespaces import flatten

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
res = requests.get(url)
htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

usd = float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(3)').text)
hkd = float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(3)').text)
jpy = float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(3)').text)


#
while True:
    mode = input('換算美金請按1、港幣2、日幣3，或輸入q結束程式：')

    if mode == 'q':
        print('掰!!')
        break
    twd = float(input('請輸入台幣金額：'))
    result = ''
    if mode == '1':
        result = round(twd / usd)
        print(f'台幣{twd}約為美金{result}')
    if mode == '2':
        result = round(twd / hkd)
        print(f'台幣{twd}約為港幣{result}')
    if mode == '3':
        result = round(twd / jpy)
        print(f'台幣{twd}約為日幣{result}')

