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


# not in
string = input()
numbers = '1234567890'
count = 0
for c in string:
    if c == c.lower() and c not in numbers:
        count += 1
print(count)


# Теория из курса
s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')


s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')


# С помощью оператора IN мы можем упростить следующий код, проверяющий,
# что переменная s равна одному из пяти символов:
# 'a', 'e', 'i', 'o', 'u':

if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')

# до вида:

if len(s) == 1 and s in 'aeiou':
    print('YES')