# Построчный список, состоящий из n списков
# Мое решение
array = [i + 1 for i in range(int(input()))]

for li in array:
    print(array)

# Варианты
n = int(input())
for _ in range(n):
    print(list(range(1, n + 1)))

print('=' * n * 3)

result = []
for _ in range(n):
    result.append(list(range(1, n + 1)))
print(*result, sep='\n')

# Построчный список 2, состоящий из n списков
n = int(input())
for i in range(1, n + 1):
    print(list(range(1, i + 1)))

print('=' * n * 3)

# Другой вариант
result = []
for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))
print(*result, sep='\n')


# Треугольник Паскаля 1
number = int(input())
array = [[1]]

for i in range(1, number + 1):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = array[i - 1][j - 1] + array[i - 1][j]
    array.append(row)

print(array[-1])

# Треугольник Паскаля 2
number = int(input())
array = []

for i in range(number):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = array[i - 1][j - 1] + array[i - 1][j]
    array.append(row)

for c in array:
    print(*c)


# Упаковка дубликатов
s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)
# или
string = input().split()

array = [[string[0]]]
for i in range(1, len(string)):

    if string[i] == string[i - 1]:
        array[-1].append(string[i])
    else:
        array.append([string[i]])

print(array)


# Разбиение на чанки
def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))
# Без функции
string = input().split()
number = int(input())

array = []
for i in range(0, len(string), number):
    array.append(string[i:i + number])

print(array)


# Подсписки списка
string = input().split()

array = [[]]

for i in range(len(string)):
    for j in range(len(string) - i):
        array.append(string[j:j + i + 1])

print(array)