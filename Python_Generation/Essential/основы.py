# На easy
from math import sqrt, pow

a = int(input())
b = int(input())
plus = a + b
minus = a - b
multi = a * b
divide_1 = a / b
divide_2 = a // b
divide_3 = a % b
Sqrt = sqrt(pow(a, 10) + pow(b, 10))
print(plus, minus, multi, divide_1, divide_2, divide_3, Sqrt, sep='\n')

# Индекс массы тела
weight = float(input())
height = float(input())
weight_index = weight / pow(height, 2)

if weight_index < 18.5:
    print("Недостаточная масса")
elif weight_index > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")


# Стоимость строки: один любой символ(в том числе пробел) стоит 60 копеек
# Длинное решение - не получается округление price = round(0.6 * len(string), 2)
# Со строками в одно слово(2 - 10 символов) - неправильно
string = input()
price = 60 * len(string)

if len(string) == 1:
    print('0 р. 60 коп.')
elif '00' in str(price):
    print(str(price)[:2], 'р.', str(price)[2:3], 'коп.')
else:
    print(str(price)[:2], 'р.', str(price)[2:4], 'коп.')
# или

string = input()
price = 60 * len(string)

print(f'{price // 100} р. {price % 100} коп.')

# Количество слов
string = input().split()
print(len(string))

# Зодиак
# Вспомогательный код:
# С помощью цикла определяем нулевой год(нулевой индекс)
for i in range(2004, -1, -12):
# С 2004 по 0 год через каждые 12 лет - Обезьяна
    print(i)

# Основной код
year = int(input())
# Нулевой индекс списка - Обезьяна
array = [
    'Обезьяна', 'Петух', 'Собака', 'Свинья',
    'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон',
    'Змея', 'Лошадь', 'Овца'
]
# Деление числа на длину списка - дает индекс этого списка
animal = year % len(array)
print(array[animal])


# Переворот числа
number = input()

if '000' in number and len(number) == 5:
    print(number[::-1][-2:])
elif len(number) == 5:
    print(number[::-1])
else:
    print(number[0] + number[1:][::-1])
# или
number = input()

new_number = int(number[:-5] + number[-5:][::-1])
print(new_number)


# Standard American Convention
number = input()[::-1]
counter = 0
array = []
for i in number:
    counter += 1
    if counter == 3:
        array.append(i)
        array.append(',')
        counter = 0
    else:
        array.append(i)

print(''.join(array)[::-1].strip(','))




# Задача Иосифа Флавия
n = int(input())
k = int(input())

counter = 0

for i in range(1, n + 1):
    counter = (counter + k) % i

print(counter + 1)