# Напишите программу, которая выводит все целые числа от m до n включительно
m = int(input())
n = int(input())

for i in range (m, n+1):
    print(i)

# Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае
m = int(input())
n = int(input())

if m < n:
    for i in range (m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
elif m == n:
    print(m)

# Второй вариант
m = int(input())
n = int(input())
if m > n:
    for i in range(m, n - 1, -1):
        print(i)
else:
    for i in range(m, n + 1, +1):
        print(i)

# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные целые числа от m до n включительно в порядке убывания
m = int(input())
n = int(input())

for i in range(m, n-1, -1):
    if i % 2 != 0:
        print(i)

# Напишите программу, которая выводит все целые числа от m до n включительно, при этом:
# число кратно 17
# число оканчивается на 9
# число кратно 3 и 5 одновременно
m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)

# Второй вариант
m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)

# Дано натуральное число n.
# Напишите программу, которая выводит таблицу умножения на n (от 1 до 10 включительно)
n = int(input())

for i in range(n, n + 1):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)