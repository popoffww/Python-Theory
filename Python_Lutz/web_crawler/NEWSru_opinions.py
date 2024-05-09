import requests
from bs4 import BeautifulSoup

def page_spider(max_pages):
    page = 1
    while page <= max_pages:
       url = 'http://blog.classic.newsru.com/?page' + str(page)
       source_code = requests.get(url)
       plain_text = source_code.text
       soup = BeautifulSoup(plain_text)  # (plain_text, 'html.parser') на случай ошибки
       for link in soup.findAll('a', {'class': 'articletitle'}):  # articletitle ('эта же переменная в цикле for на 24 строке')
           href = 'http://blog.classic.newsru.com' + link.get('href')
           title = link.string
           print(href)   # закомментировать, если раскомментировать get_single_item_data(href)
           print(title)  # закомментировать, если раскомментировать get_single_item_data(href)
           # get_single_item_data(href)
       page += 1

       # ВСЕ ССЫЛКИ СТРАНИЦЫ
# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for articletitle  in soup.findAll('div', {'class': 'mainhead'}):  # articletitle ('эта же переменная в цикле for на 11 строке')
#         print(articletitle.string)
#     for link in soup.findAll('a'):
#         href = 'http://blog.classic.newsru.com' + link.get('href')
#         print(href)

page_spider(1)
