# Квадраты ключей
result = {}

for i in range(1, 16):
    result[i] = result.get(i, i ** 2)
    # или
    # result.setdefault(i, i ** 2)
print(result)

# Сумма значений
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value
print(result)


# Количество вхождений символов строки
text = 'footballcyberpunkextraterritorialityconversationa' \
       'listblockophthalmoscopicinterdependencemamauserfff'

result = {}

for sym in text:
    result[sym] = result.get(sym, 0) + 1
print(result)


# Наиболее часто встречающееся слово строки
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon ' \
    'pomegranate banana banana orange barley apricot plum grapefruit banana quince ' \
    'strawberry barley grapefruit banana grapes melon strawberry apricot currant ' \
    'currant gooseberry raspberry apricot currant orange lime quince grapefruit barley ' \
    'banana melon pomegranate barley banana orange barley apricot plum banana quince lime ' \
    'grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate ' \
    'banana banana orange apricot barley plum banana grapefruit banana quince currant orange ' \
    'melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()

d = {}

for word in s:
    d[word] = s.count(word)

result = {}

maximum = max(d.values())

for key, value in d.items():
    if value == maximum:
        result[key] = value

print(min(result))


# Наименее часто встречающееся слово строки
s = input().lower().split()

array = [el.strip(".,!?;:-") for el in s]
d = {}

for word in array:
    d[word] = array.count(word)

result = {}

minimum = min(d.values())

for key, value in d.items():
    if value == minimum:
        result[key] = value

print(min(result))


# Исправление дубликатов
# Необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался
s = input().split()

dct = {}
array = []

for i in s:
    if i not in array:
        array.append(i)
    else:
        dct[i] = dct.get(i, 0) + 1
        array.append(i + '_' + str(dct[i]))

print(*array)


# Владельцы собак
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

# 1 способ
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0])

print(result)

# 2 способ
for pet, first_name, second_name, age in pets:
    owner = (first_name, second_name, age)

    result.setdefault(owner, []).append(pet)

# 3 способ
for pet, first_name, second_name, age in pets:
    owner = (first_name, second_name, age)

    result[owner] = result.get(owner, []) + [pet]