import bs4
import requests

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

res = requests.get(url)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')


twd = float(input('請輸入台幣金額：'))
# print(htmlfile)
# print(htmlfile.find('h1').text)
# print(htmlfile.find('p'))
# print(htmlfile.find('p',class_='text-info').text)
title = htmlfile.find('h1').text

# print(title)
print(title.strip())

# print(htmlfile.select_one('tbody tr td:nth-of-type(3)'))
# exc = htmlfile.select('tbody tr td:nth-of-type(3)')
# for e in exc:
#     print(e.text)

# exc2 = htmlfile.select('tbody tr td:nth-of-type(5)')
# for e in exc2:
#     print(e.text.strip())

# datas = htmlfile.find('tbody').find_all('tr')
datas = htmlfile.select('tbody tr')
# print(datas)
for data in datas:
    # print(data.select_one('td:nth-of-type(1) div.visible-phone').text)
    t = data.select_one('td:nth-of-type(1) div.visible-phone').text.strip()
    exc = data.select_one('td:nth-of-type(3)').text.strip()
    result = twd / float(exc)
    print(f'{t}:{exc} 台幣{twd}約等於{t} - {round(result)}')
    print('-'*10)