# Анаграммы 1
s_1 = sorted(input())
s_2 = sorted(input())

dct_1 = dict(zip(range(len(s_1)), s_1))
dct_2 = dict(zip(range(len(s_2)), s_2))

if dct_1 == dct_2:
    print("YES")
else:
    print('NO')


# Анаграммы 2
s_1 = sorted([i for i in input().lower() if i.isalpha()])
s_2 = sorted([i for i in input().lower() if i.isalpha()])

dct_1 = dict(zip(range(len(s_1)), s_1))
dct_2 = dict(zip(range(len(s_2)), s_2))

if dct_1 == dct_2:
    print("YES")
else:
    print('NO')





# Словарь синонимов
n = int(input())
array = [input().split() for _ in range(n)]
word = input()
dct = {}

for key, value in array:
    dct.setdefault(key, value)
    if word == value:
        print(key)
    elif word == key:
        print(value)
# Изящное решение
words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])


# Страны и города
dct = {}

for _ in range(int(input())):
    land, *cities = input().split()
    dct[land] = cities

for _ in range(int(input())):
    city = input()
    for land, cities in dct.items():
        if city in cities:
            print(land)


# Телефонная книга
dct = {}
for _ in range(int(input())):
    tel, name = input().lower().split()
    dct[name] = dct.get(name, []) + [tel]

for _ in range(int(input())):
    enter = input().lower()
    print(*dct.get(enter, ['абонент не найден']))


# Секретное слово
s = input()
dct = {}

for _ in range(int(input())):
    value, key = input().split(': ')
    dct[int(key)] = value

for el in s:
    print(dct[s.count(el)], end='')


# Словарь программиста
dct = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    dct[key.lower()] = value

for _ in range(int(input())):
    key = input().lower()
    print(dct.get(key, 'Не найдено'))