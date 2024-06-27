import string
import random
from random import randrange as r
# IP-адрес
def generate_ip():

    return f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'

print(generate_ip())
# или
def generate_ip():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'


# Почтовый индекс - LetterLetterNumber_NumberLetterLetter
def generate_index():

    return f'{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randrange(100)}_{random.randrange(100)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}'

print(generate_index())


# 100 лотерейных билетов
for i in range(100):
    for j in range(7):
        number = random.randint(1, 9)
        print(number, end='')
    print()
# или
for _ in range(100):
    print(random.randint(1000000,9999999))
# или
print(*r(range(int(1e6), int(1e7)), 100), sep='\n')


# Анаграмма
word = input()
s = ''.join(random.sample(word, len(word)))
print(s)


# Бинго
number = random.sample(list(range(1, 76)), 25)

matrix = [number[i: i + 5] for i in range(0, 21, 5)]
matrix[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# Тайный друг
array = [input() for _ in range(int(input()))]
random.shuffle(array)

for i in range(len(array)):

    print(array[i - 1], '-', array[i])


# Генератор паролей 1
# в каждом пароле необязательно должна присутствовать хотя бы одна цифра
# и буква в верхнем и нижнем регистре
def generate_password(length):

    password = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    password = ''.join([sym for sym in password if sym not in 'lIoO'])
    return ''.join(random.sample(password, length))


def generate_passwords(count, length):

    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


# Генератор паролей 2
# в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре
import random
import string

def generate_password(length):

    up = [sym for sym in string.ascii_uppercase if sym not in 'IO']
    low = [sym for sym in string.ascii_lowercase if sym not in 'lo']
    num = list(string.digits[2:])
    sym = up + low + num

    password = [random.choice(i) for i in(up, low, num)]
    password += [random.choice(sym) for i in range(length - 3)]

    return ''.join(password)


def generate_passwords(count, length):

    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')