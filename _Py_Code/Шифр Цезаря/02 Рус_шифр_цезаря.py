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