print('"Python is a great language!"' + ', said Fred. ' + '"'"I don't ever", end= ' remember having this much fun before."')


name_1 = input()
name_2 = input()
print('Hello' + ' ' + name_1 + ' ' + name_2 + '!' + ' You have just delved into Python')


team = input()
length = len(team)
print('Футбольная команда' + ' ' + team + ' ' + 'имеет длину' + '', length, 'символов')

team = input()
length = str(len(team))
print('Футбольная команда' + ' ' + team + ' ' + 'имеет длину' + ' ' + length + ' ' + 'символов')


# Даны названия трех городов. Напишите программу,
# которая определяет самое короткое и самое длинное название города
city_1 = input()
city_2 = input()
city_3 = input()

length_1 = len(city_1)
length_2 = len(city_2)
length_3 = len(city_3)

max_length = max(length_1, length_2, length_3)
min_length = min(length_1, length_2, length_3)

if min_length == length_1 and max_length == length_2:
    print(city_1, city_2, sep='\n')
elif min_length == length_2 and max_length == length_1:
    print(city_2, city_1, sep='\n')

elif min_length == length_1 and max_length == length_3:
    print(city_1, city_3, sep='\n')
elif min_length == length_3 and max_length == length_1:
    print(city_3, city_1, sep='\n')

elif min_length == length_2 and max_length == length_3:
    print(city_2, city_3, sep='\n')
elif min_length == length_3 and max_length == length_2:
    print(city_3, city_2, sep='\n')

# Второй вариант
city_1 = input()
city_2 = input()
city_3 = input()

min_length = min(len(city_1), len(city_2), len(city_3))
max_length = max(len(city_1), len(city_2), len(city_3))

if len(city_1) == min_length:
    print(city_1)
elif len(city_2) == min_length:
    print(city_2)
else:
    print(city_3)

if len(city_1) == max_length:
    print(city_1)
elif len(city_2) == max_length:
    print(city_2)
else:
    print(city_3)

a1 = input()
a2 = input()
a3 = input()


# Вводятся 33 строки в случайном порядке.
# Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию
length_1 = len(a1)
length_2 = len(a2)
length_3 = len(a3)

max_length = max(length_1, length_2, length_3)
min_length = min(length_1, length_2, length_3)
mid_length = (length_1 + length_2 + length_3) - (max_length + min_length)

if mid_length - min_length == max_length - mid_length:
    print('YES')
else:
    print('NO')


# В такой записи Python ищет полное совпадение
string = input()
if 'синий' in string:
    print('YES')
else:
    print('NO')

# А в такой, достаточно одного совпадения
string = input()
if string in 'синий':
    print('YES')
else:
    print('NO')


string = input()
if 'суббота' in string:
    print('YES')
elif 'воскресенье' in string:
    print('YES')
else:
    print('NO')

# Email
string = input()
if '@' in string and '.' in string:
    print('YES')
else:
    print('NO')