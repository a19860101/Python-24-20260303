import requests

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=846e44e1-8cc5-4893-ad87-c79d2d383706&limit=1000&sort=ImportDate%20desc&format=JSON'

response = requests.get(url, verify=False)

result = response.json()

for item in result:
    print(item['sitename'])
    print(item['aqi'])
