# Равнобедренный треугольник
def draw_triangle():

    for i in range(8):
        print(' ' * (8 - 1 ) + '*' * (1 + i * 2))

draw_triangle()


# 1000 рублей за первый товар и 120 рублей за каждый последующий
def get_shipping_cost(quantity):

    return 1000 + (quantity - 1) * 120

n = int(input())
print(get_shipping_cost(n))


# Биномиальный коэффициент
from math import factorial

def compute_binom(n, k):

    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = int(input())
k = int(input())

print(compute_binom(n, k))


# Число словами
def number_to_words(num):

    array = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', '']
    array_2 =['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num <= 20:
        return array[num - 1]
    else:
        return array_2[num // 10 - 2] + ' ' + array[num % 10 - 1]

n = int(input())

print(number_to_words(n))


# Искомый месяц
def get_month(language, number):

    rus = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        return rus[number - 1]
    else:
        return eng[number - 1]

lan = input()
num = int(input())

print(get_month(lan, num))


# Магические даты
def is_magic(date):

    string = date.split('.')

    if int(string[0]) * int(string[1]) == int(string[2]) % 100:
        return  True
    return False

date = input()

print(is_magic(date))


# Панграммы
def is_pangram(text):

    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't',                  'u', 'v', 'w', 'x', 'y', 'z']
    text = text.replace(' ', '')
    text = text.lower()

    for c in array:
        if c not in text:
            return False
    return True

text = input()

print(is_pangram(text))