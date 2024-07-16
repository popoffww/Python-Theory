import string
# Латинский алфавит
alpahabet = 'abcdefghijklmnopqrstuvwxyz'
alpahabet_power = len(alpahabet)
decipher = ''
cipher = input('Введите зашифрованную строку:\n').lower()
shift = int(input('Введите сдвиг(число):\n'))

for i in range(len(cipher)):
    if cipher[i].isalpha():
        # Для зашифровки
        letter = (alpahabet.index(cipher[i]) + shift) % alpahabet_power
        # Для расшифровки
        # letter = (alpahabet.index(cipher[i]) - shift) % alpahabet_power
        decipher += alpahabet[letter]
    else:
        decipher += cipher[i]

print(decipher.capitalize())



alphabet = string.ascii_lowercase
alphabet_power = len(alphabet)
result = ""
input_string = input("Введите исходный текст:\n").lower()
shift = int(input("Введите сдвиг - смещение(число), на которое закодирован текст:\n"))

for i in range(len(input_string)):
    if input_string[i].isalpha():
        # letter = (alphabet.index(input_string[i]) + shift) % alphabet_power
        letter = (alphabet.index(input_string[i]) - shift) % alphabet_power
        result += alphabet[letter]
    else:
        result += input_string[i]

print(result.capitalize())