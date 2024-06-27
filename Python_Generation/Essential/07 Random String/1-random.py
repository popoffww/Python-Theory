import random
# Орел-Решка
n = int(input())    # количество попыток

for i in range(n):
    number = random.randint(1,  10)
    if number % 2 == 0:
        print('Орел')
    else:
        print('Решка')

# Кубик
n = int(input())

for i in range(n):
    number = random.randint(1,  6)
    print(number)

# Пароль
length = int(input())    # длина пароля

password = ''
for _ in range(length):
    if random.randint(0, 1) == 1:
        password += chr(random.randint(65, 90))
    else:
        password += chr(random.randint(97, 122))

print(password)

# Спортлото 7 из 49
sport_loto = []
for _ in range(7):
    numbers = random.randint(1, 49)
    sport_loto.append(numbers)

print(*sorted(sport_loto), end=' ')
# или
s = set()

while len(s) < 7:
    s.add(random.randint(1, 49))

print(*sorted(s))