import random
# Переворот строки
# Вам доступен текстовый файл text.txt с одной строкой текста
with open('text.txt', encoding='utf-8') as file:
    for line in file:
        print(line[::-1].strip())
# или
line = open('text.txt', encoding='utf-8')
print(line.read()[::-1])
line.close()


# Обратный порядок
# Вам доступен текстовый файл text.txt, в котором записаны строки текста
with open('text.txt', encoding='utf-8') as file:
    for line in file.readlines()[::-1]:
        print(line.strip())


# Длинные строки
# One
# Twenty one
# Two
# Twenty two
with open('lines.txt', encoding='utf-8') as file:
    line = file.readlines()
    maximum = max(map(len, line))
    print(*filter(lambda x: len(x) == maximum, line), sep='')


# Сумма чисел в строках
# 2 1
#      3    40
#  10       7
with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        print(sum([int(num) for num in line.split()]))


# Сумма чисел в файле
#  123   jhjk
# bhjip456qwerty
# 1x2y3 4 5 6
# sfsd 0 dfgfd
# 10abc20de30pop5 5 5 5
with open('nums.txt', encoding='utf-8') as file:
    s = 0
    k = '0'
    for i in file.read():
        if i.isdigit():
            k += i
        else:
            s += int(k)
            k = '0'

    print(s)


# Статистика по файлу
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
with open('file.txt', encoding='utf-8') as file:
    text = file.read()
    letters = len(list(filter(lambda x: x.isalpha(), text)))
    words = len(text.split())
    lines = len(text.splitlines())

    print(f'Input file contains: \n{letters} letters \n{words} words \n{lines} lines')


# Напишите программу, которая c помощью модуля random создает 3 случайные пары:
# имя + фамилия, а затем выводит их, каждую на отдельной строке
# first_names.txt:
# Aaron
# Abdul
# Abe
# Abel
# Abraham
# Albert
# last_names.txt
# Abramson
# Adamson
# Adderiy
# Addington
# Adrian
# Albertson
# Einstein
with open('first_names.txt', encoding='utf-8') as first_names, open('last_names.txt', encoding='utf-8') as last_names:

    names = first_names.readlines()
    surnames = last_names.readlines()

    for i in range(3):
        print(f'{random.choice(names).strip()} {random.choice(surnames).strip()}')


# Необычные страны
# Файл population.txt
with open('population.txt', encoding='utf-8') as file:
    line = [el.split('\t') for el in file]

for c in line:
    if c[0].startswith('G') and int(c[1]) > 500_000:
        print(c[0])


# CSV-файл
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
def read_csv():
    with open('text.txt', encoding='utf-8') as file:
        key = [line.strip() for line in file.readline().split(',')]
        value = [line.strip().split(',') for line in file.readlines()]

    return [dict(zip(key, i)) for i in value]

print(read_csv())