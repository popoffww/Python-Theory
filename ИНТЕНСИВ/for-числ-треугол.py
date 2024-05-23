# Таблица сложения-умножения
n = int(input())
# for i in range(n, n + 1):
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, "+", j, "=", i + j)
    print()

print('=' * 10)

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)
    print()

# Численный треугольник
number = int(input())

for i in range(number):
    for j in range(i + 1):
        print(i + 1, end=' ')
    print()

print('=' * 10)

for i in range(number):
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()

print('=' * 10)

counter = 0
for i in range(1, number + 1):
    for j in range(i):
        counter += 1
        print(counter, end=' ')
    print()

print('=' * 10)

for i in range(1, number + 1):
    for j in range(i):
        print(j + 1, end=' ')
    for k in range(i - 1, 0, -1):
        print(k, end=' ')
    print()

