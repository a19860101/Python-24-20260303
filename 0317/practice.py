import requests

url = 'https://itunes.apple.com/search'

my_params = {
    'term':'周杰倫',
    'entity':'album',
    'country':'TW'
}

res = requests.get(url, params=my_params)

data = res.json()

for item in data['results']:
    # print(item)
    print(f'專輯名稱:{item.get('collectionName')} | 歌手:{item.get('artistName')} | 發行日期:{item.get('releaseDate')[:10]}')