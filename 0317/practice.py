import requests

url = 'https://itunes.apple.com/search'

while True:

    term = input('請輸入關鍵字或輸入q結束程式:')

    if term == 'q':

        print('BYE!')
        break

    my_params = {
        'term':term,
        'entity':'album',
        'country':'TW'
    }

    res = requests.get(url, params=my_params)

    data = res.json()
    print(data)
    for item in data['results']:
        print(item)
        print(f'專輯名稱:{item.get('collectionName')} | 歌手:{item.get('artistName')} | 發行日期:{item.get('releaseDate')[:10]}')

    print('*' * 100)