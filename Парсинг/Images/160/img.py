import requests

for i in range(1, 161):
    with open(f'Img/{i}.png', 'wb') as file:
        response = requests.get(url=f'http://parsinger.ru/img_download/img/ready/{i}.png')
        file.write(response.content)