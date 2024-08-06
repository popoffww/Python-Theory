import requests

with open('judo.jpg', 'wb') as file:
    response = requests.get('https://img.olympics.com/images/image/private/t_1-1_760/f_auto/primary/qk4itf3dlofsxisxcck0')
    file.write(response.content)