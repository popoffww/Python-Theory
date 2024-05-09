# Латинский алфавит
for i in range(26):
    print(chr(ord('A') + i))


# Символы в диапазоне
a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(chr(i), end=' ')


# Простой шифр
string = input()

for i in range(len(string)):
    print(ord(string[i]), end=' ')

# Шифр Цезаря
number = int(input())
string = input()

for c in string:
    if ord(c) - number < 97:
        print(chr(ord(c) - number + 26), end='')
    else:
        print(chr(ord(c) - number), end='')