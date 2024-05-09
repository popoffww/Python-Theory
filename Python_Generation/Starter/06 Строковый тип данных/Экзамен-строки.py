s = 'Python rocks!'
print(len(s))

s = 'Python rocks!'
print(s[3])

s = 'Python rocks!'
print(s[1:5])

s = '    Python rocks!     '
print(s.strip())

s = 'Python rocks!'
print(s.upper())

s = 'Python rocks!'
print(s.replace('o', '@'))


# Напишите программу, которая удаляет из нее все символы с индексами, кратными 3,
# то есть символы с индексами 0, 3, 6, ...
string = input()
for i in range(len(string)):
    if i % 3 == 0:
        continue
    print(string[i], end='')


# Напишите программу, которая заменяет все вхождения цифры 1 на слово one
string = input()
if '1' in string:
    print(string.replace('1', 'one'))
else:
    print(string)


# Напишите программу, которая удаляет все вхождения символа @
string = input()
if '@' in string:
    print(string.replace('@', ''))
else:
    print(string)


# Напишите программу, которая выводит индекс второго вхождения буквы f
string = input()
if string.count('f') == 0:
    print('-2')
elif string.count('f') == 1:
    print('-1')
else:
    string = string.replace('f', '', 1)
    print(string.find('f') + 1)


# Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов,
# заключенную между первым и последним вхождением буквы h
string = input()

before = string[:string.find('h')]
after = string[string.rfind('h') + 1:]
reverse = string[string.find('h'):string.rfind('h') + 1][::-1]

print(before, reverse, after, sep='')

# Второй вариант
string = input()

first = string.find('h')
second = string.rfind('h')
print(string[:first], string[second:first:-1], string[second:], sep = "")