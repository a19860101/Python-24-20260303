import requests
import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=846e44e1-8cc5-4893-ad87-c79d2d383706&limit=1000&sort=ImportDate%20desc&format=JSON'

response = requests.get(url, verify=False)

result = response.json()

# print(len(result))

# print(result)

top10 = sorted(result, key=lambda x: int(x['aqi']),reverse=True)[:10]

aqi_y = []
aqi_x = []
colors = []

for i in result:
    # print(i['sitename'],i['county'],i['aqi'])
    aqi_y.append(int(i['aqi']))
    aqi_x.append(i['sitename'])

    if int(i['aqi']) > 60:
        colors.append('red')
    elif int(i['aqi']) > 40:
        colors.append('orange')
    elif int(i['aqi']) > 20:
        colors.append('greenyellow')
    else:
        colors.append('green')

print(aqi_x)
print(aqi_y)

plt.yticks(range(0,120,10))
plt.ylim(0,120)
plt.grid(axis='y')
plt.bar(aqi_x,aqi_y, color=colors)

plt.show()
