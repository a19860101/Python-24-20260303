import requests
import bs4

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
res = requests.get(url)
htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

usd = float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(3)').text)
hkd = float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(3)').text)
jpy = float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(3)').text)
krw = float(htmlfile.select_one('tbody tr:nth-of-type(16) td:nth-of-type(3)').text)

rates = {
    '1': (usd, '美金'),
    '2': (hkd, '港幣'),
    '3': (jpy, '日幣'),
    '4': (krw, '韓幣')
}



#
while True:
    mode = input('換算美金請按1、港幣2、日幣3、韓幣4，或輸入q結束程式：')

    if mode == 'q':
        print('掰!!')
        break
    twd = float(input('請輸入台幣金額：'))

    result = round(twd / rates[mode][0])

    print(f'台幣{twd}約為{rates[mode][1]}{result:,}')

