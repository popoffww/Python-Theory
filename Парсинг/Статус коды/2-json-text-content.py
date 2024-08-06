import requests

r = requests.get("https://parsinger.ru/3.4/2/index.html")
r.encoding = "utf-8"
print(r.text)


# Получение и анализ данных о погоде
url = 'https://parsinger.ru/3.4/1/json_weather.json'

data = {}
r = requests.get(url)
if r.status_code == 200:
    r = r.json()
    for i in r:
        data[i['Дата']] = int(i['Температура воздуха'].replace('°C',''))

print(sorted(data.items(), key = lambda x: x[1])[0])


# или
url = 'https://parsinger.ru/3.4/1/json_weather.json'

response = requests.get(url)

dictionary = {}
if response.status_code == 200:
    for i in response.json():
        dictionary[int(str(i['Температура воздуха']).replace('°C', ''))] = i['Дата']
else:
    print(f"Ошибка статус кода {response.status_code}")

print(dictionary[min(dictionary)])