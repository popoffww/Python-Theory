# Проверь никнейм
nickname = input()

if 5 <= len(nickname) <= 15 and nickname[0] == '@' and nickname == nickname.lower() and nickname[1:].isalnum():
    print('Correct')
else:
    print('Incorrect')


# Плохие комментарии
# Мой вариант
number = int(input())

for i in range(number):
    string = input()
    if string.isspace() or string == '':
        print(i + 1,':',' ', 'COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i + 1,':',' ', string, sep='')


# Второй вариант
for i in range(1, int(input()) + 1):
    string = input()
    if string.isspace() or string == '':
        print(f'{i}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i}: {string}')


# Автомобильный номер
string = input().upper()
alphabet = 'АВЕКМНОРСТУХ'
flag = 'NO'

if 9 <= len(string) <= 10:
    letters = string[0] + string[4:6]
    ciffres = string[1:4] + string[7:10]
    sign = string[6]
    if ciffres.isdigit() and sign == '_':
        flag = 'YES'

    for c in letters:
        if c not in alphabet:
            flag = 'NO'
            break

print(flag)

# Изящный вариант
'''
Пусть:
    0 - буква
    1 - цифра
    _ - _
    2 - остальные символы
Тогда нужным формат описывается как 011100_11 или 011100_111
'''

alphabet = 'АВЕКМНОРСТУХ'
ciffres = '0123456789'
string = input()

# переводим в проверочный формат
result = ''
for symbol in string:
    if symbol in alphabet:
        result += '0'
    elif symbol in ciffres:
        result += '1'
    elif symbol == '_':
        result += '_'
    else:
        result += '2'

if result in ['011100_11', '011100_111']:
    print('YES')
else:
    print('NO')