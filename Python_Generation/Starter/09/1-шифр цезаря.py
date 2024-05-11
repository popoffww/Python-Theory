# Латинский алфавит
alpahabet = 'abcdefghijklmnopqrstuvwxyz'
alpahabet_power = len(alpahabet)
decipher = ''
cipher = input('Введите зашифрованную строку:\n').lower()
shift = int(input('Введите сдвиг(число):\n'))

for i in range(len(cipher)):
    if cipher[i].isalpha():
        # Для зашифровки
        # letter = (alpahabet.index(cipher[i]) + shift) % alpahabet_power
        # Для расшифровки
        letter = (alpahabet.index(cipher[i]) - shift) % alpahabet_power
        decipher += alpahabet[letter]
    else:
        decipher += cipher[i]

print(decipher.capitalize())


# Русский алфавит
alpahabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alpahabet_power = len(alpahabet)
decipher = ''
cipher = input('Введите зашифрованную строку:\n').lower()
shift = int(input('Введите сдвиг(число):\n'))

for i in range(len(cipher)):
    if cipher[i].isalpha():
        # Для зашифровки
        # letter = (alpahabet.index(cipher[i]) + shift) % alpahabet_power
        # Для расшифровки
        letter = (alpahabet.index(cipher[i]) - shift) % alpahabet_power
        decipher += alpahabet[letter]
    else:
        decipher += cipher[i]

print(decipher.capitalize())


# 9.7 Строки в памяти компьютера, таблица символов Unicode
number = int(input()) # сдвиг
string = input()

for c in string:
    if ord(c) - number < 97:
        print(chr(ord(c) - number + 26), end='')
    else:
        print(chr(ord(c) - number), end='')



# Аве, Цезарь
n = input()
s = n

for i in s:
    if i in '.,*@!?"-':
        s = s.replace(i, '')

x = [len(j) for j in s.split()]
counter = 0
word = ''

for c in n:
    number = ord(c)
    if c == ' ':
        counter += 1
        word += c
    elif 65 <= number <= 90:
        if number + x[counter] > 90:
            word += chr(number + x[counter] - 26)
        else:
            word += chr(number + x[counter])
    elif 97 <= number <= 122:
        if number + x[counter] > 122:
            word += chr(number + x[counter] - 26)
        else:
            word += chr(number + x[counter])
    else:
        word += c

print(word)