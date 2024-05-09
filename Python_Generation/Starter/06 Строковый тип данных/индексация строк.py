# Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик
string = input()
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])

# Напишите программу, которая выводит в столбик элементы строки в обратном порядке
string = input()[::-1]
for c in string:
        print(c)

string = input()
for i in range(len(string) - 1, -1, -1):
    print(string[i])

# На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке).
# Напишите программу, которая выводит инициалы человека
name = input()
surname = input()
surname_2 = input()

print(surname[0], name[0], surname_2[0], sep='')

# На вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки
string = input()
total = 0

for c in string:
# Если в вводе строке цифры; с буквами и символами будет ошибка
        total += int(c)
print(total)

# Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
# В противном случае вывести сообщение «Цифр нет» (без кавычек)
string = input()
flag = False
for c in string:
        if c in '1234567890':
                flag = True
if flag:
        print('Цифра')
else:
        print('Цифр нет')


# Второй вариант
string = input()
flag = False
for i in range(len(string)):
    if string[i] in '1234567890':
        flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')


# Напишите программу, которая подсчитывает количество цифр в данной строке
string = input()
total = 0
for i in range(len(string)):
    if string[i] in '1234567890':
        total += 1
print(total)


# Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *
string = input()
plus = 0
star = 0
for i in range (len(string)):
    if '+' in string[i]:
        plus += 1
    elif '*' in string[i]:
        star += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')


# На вход программе подается одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных звуков
string = input()
letters_1 = 0
letters_2 = 0
for c in string:
    if c in 'ауоыиэяюеАУОЫИЭЯЮЕ':
        letters_1 += 1
    elif c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        letters_2 += 1

print('Количество гласных букв равно', letters_1)
print('Количество согласных букв равно', letters_2)


# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов
string = input()
result = 0
for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        result += 1
print(result)


# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления
number = int(input())

string = ''
string_2 = ''

while number > 0:
    string += str(number % 2)
    number //= 2
for i in range(-1, -len(string) - 1, -1):
    string_2 += string[i]
print(string_2)
