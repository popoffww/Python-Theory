import string
# Перевод десятичного числа в двоичное
n = int(input())

to_bin = ''
res = ''

while n > 0:
    to_bin += str(n % 2)
    n //= 2

print(to_bin[::-1])

for i in range(-1, -len(to_bin) - 1, -1):
        res += to_bin[i]

print(res)


# Деление строки попалам
s = input()

a = s[:(len(s) + 1) // 2]
b = s[(len(s) + 1) // 2:]

print(b + a)


# Палиндром
s = input()

if s == s[::-1]:
    print('Палиндром')
else:
    print('Нет - не палиндром')


# Есть число в строке или нет?
s = input()

for c in s:
    # if с in '012345667689':
    if c in string.digits:
        print('Есть цифры')
        break
else:
    print('Нет цифр')