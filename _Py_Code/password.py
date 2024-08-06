import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

yes = ['yes', 'y', 'да', 'д']

number_pass = int(input('Укажите количество паролей, которое нужно сгенерировать: '))
length = int(input('Укажите требуемую длину пароля: '))

if input('Включить в пароль цифры? ') in yes:
    chars += digits
if input('Включить в пароль прописные буквы? ') in yes:
    chars += uppercase_letters
if input('Включить в пароль строчные буквы? ') in yes:
    chars += lowercase_letters
if input('Включить в пароль специальные символы? ') in yes:
    chars += punctuation
if input('Исключить неоднозначные символы? ') in yes:
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

for i in range(1, number_pass + 1):
    print(f'Пароль №{i}:', generate_password(length, chars))