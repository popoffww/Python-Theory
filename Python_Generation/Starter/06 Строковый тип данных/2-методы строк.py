# На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней
string = input()

print(string.count(' ') +1)

# На вход программе подается строка, состоящая из символов А, Г, Ц, Т, а, г, ц, т
# Сколько аденина, гуанина, цитозина и тимина входит в данную строку
string = input().lower()

print('Аденин:', string.count('а'))
print('Гуанин:', string.count('г'))
print('Цитозин:', string.count('ц'))
print('Тимин:', string.count('т'))


# В первой строке подаётся число n – количество сообщений, в последующих n строках вводятся строки,
# содержащие латинские строчные буквы и цифры.
# Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза
number = int(input())
count = 0
for i in range(number):
    string = input()
    if string.count('11') >= 3:
        count += 1
print(count)

# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru
string = input()
if string.endswith('.com') or string.endswith('.ru'):
    print('YES')
else:
    print('NO')

# Напишите программу, которая подсчитывает количество цифр в данной строке
# Мой вариант
string = input()
total = 0
for i in range(len(string)):
    if string[i] in '1234567890':
        total += 1
print(total)

# Второй вариант
string = input()
counter = 0
for c in '1234567890':
    counter += string.count(c)
print(counter)

# Третий вариант
string = input()
counter = 0
for i in range(10):
    counter += string.count(str(i))
print(counter)

# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru
string = input()
if string.endswith('.com') or string.endswith('.ru'):
    print('YES')
else:
    print('NO')


# Первое и последнее вхождение буквы f
string = input()

if string.count('f') == 1:
    print(string.index('f'))
elif string.count('f') > 1:
    print(string.index('f'), string.rindex('f'), end=' ')
else:
    print('NO')


# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними
string = input()

before = string[:string.find('h')]
after = string[string.rfind('h') + 1:]

print(before, after, sep='')


# Напишите программу, которая выводит на экран символ, который появляется наиболее часто
string = input()

counter = 0
result = ''

for i in range(len(string)):
    string_2 = string.count(string[i])
    if string_2 >= counter:
        counter = string_2
        result = string[i]

print(result)