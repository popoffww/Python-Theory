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