import requests

url = 'https://itunes.apple.com/search'

my_params = {
    'term':'周杰倫',
    'country':'TW'
}

res = requests.get(url, params=my_params)

print(res.json())

