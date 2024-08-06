import requests
# Суммирование HTTP статус-кодов
# От https://parsinger.ru/3.3/2/1.html
# До https://parsinger.ru/3.3/2/200.html

total = 0

for i in range(1, 201):
    url = f"https://parsinger.ru/3.3/2/{i}.html"
    response = requests.get(url)
    total += response.status_code
print(total)



# Поиск рабочей ссылки и секретного кода на ней
# От https://parsinger.ru/3.3/1/1.html
# До https://parsinger.ru/3.3/1/200.html
# Секретный код: 9876316843187416358741341687416874165432
for i in range(1, 201):
    url = f"https://parsinger.ru/3.3/1/{i}.html"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        break


# Определение первой и последней доступных страниц в заданном диапазоне URL-адресов
# От https://parsinger.ru/3.3/4/1.html
# До https://parsinger.ru/3.3/4/100.html
# Первая доступная страница: 9.html
# Последняя доступная страница: 89.html
flag = False
for i in range(1, 101):
    url = f"https://parsinger.ru/3.3/4/{i}.html"
    response = requests.get(url)
    if response.status_code == 200:
        if not flag:    # if flag == False
            first_page = i
            flag = True
        else:
            last_page = i

print(f"Первая доступная страница: {first_page}.html")
print(f"Последняя  доступная страница: {last_page}.html")