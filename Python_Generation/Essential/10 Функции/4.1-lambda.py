func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# или
func = lambda x: x % 19 == 0 or x % 13 == 0

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))


func = lambda word: True if word[0] in 'aA' and word[-1] in 'aA' else False
# или
func = lambda word: word.lower().startswith('a') and word.lower().endswith('a')

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))


# Строковый аргумент является неотрицательным числом
# x.replace('.', '', 1) - замена точки на пустую строку 1(один) раз
is_non_negative_num  = lambda x: x.replace('.', '', 1).isdigit()

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))


# Строковый аргумент является числом (целым или вещественным)
is_num = lambda x: '-' not in x[1:] and \
         x.replace('.', '', 1).replace('-', '', 1).isdigit()

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))


# 6 символов
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

length_6 = list(filter(lambda word: len(word) == 6, words))
print(*sorted(length_6))


# Удаляет из списка numbers все нечетные элементы, большие 47
# Делит все четные элементы нацело на 2 (целочисленное деление – //)
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

numbers = filter(lambda x: x % 2 == 0 or x % 2 == 1 and x < 47, numbers)
numbers = map(lambda x: x // 2 if x % 2 == 0 else x, numbers)
print(*numbers)


# Сортировка производится в лексикографическом порядке(по алфавиту) по убыванию
# на основании последнего символа в названии штата
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

for i in sorted(data, key=lambda city: city[1][-1], reverse=True):
    print(f'{i[1]}: {i[0]}')


# Список по возрастанию длины слов
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

print(*sorted(data, key=lambda word: (len(word), word)))


# Наибольшее числовое значение в списке
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

max_num = max(filter(lambda x: str(x).isdigit(), mixed_list))
print(max_num)


# Противоположный цвет
# Ввод: 244 11 120
print(*list(map(lambda x: 255 - x, [int(i) for i in input().split()])))


# Значение многочлена
from functools import reduce

evaluate = lambda coeff, x: reduce(lambda s, a: s * x + a, coeff)

print(evaluate(map(int, input().split()), int(input())))

# Сортировка по неубыванию значений элементов, при этом числа должны следовать до строк
mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

# (isinstance(x, str), x) - sorted сортирует False(0), если x - цифра, True(1), если x - строка
new_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print(*new_list)
# или
new_list = sorted(filter(lambda x: type(x) == int, mixed_list)) + \
           sorted(filter(lambda x: type(x) == str, mixed_list))
print(*new_list)
