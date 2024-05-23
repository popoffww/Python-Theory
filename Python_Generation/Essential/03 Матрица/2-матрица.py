# Таблица умножения
n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# Индексы(строка и столбец) первого вхождения максимального элемента
n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

maximum = matrix[0][0]
x = 0
y = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            x = i
            y = j
print(x, y)


# На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену
n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

x, y = [int(j) for j in input().split()]

for i in range(n):
    matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]

for j in range(n):
    print(*matrix[j])


# Симметричность квадратной матрицы относительно главной диагонали
n = int(input())

matrix = []
flag = True
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and i != j:
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')


# Обмен диагоналей
n = int(input())

matrix = []
flag = True
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

for i in range(n):
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for j in range(n):
    print(*matrix[j])


# Зеркальное отображение
n = int(input())

matrix = []
flag = True
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

for i in range(n - 1, -1, -1):
    print(*matrix[i])


# Поворот матрицы на 90 градусов
n = int(input())

matrix = []
flag = True
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

for i in range(n):
    for j in range(n - 1, -1, -1):
        print(matrix[j][i], end=' ')
    print()

# Ходы коня
x, y = input()
n = 8
matrix = [['.'] * n for _ in range(n)]

y = n - int(y)
x = ord(x) - 97
matrix[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(i - y) * abs(j - x) == 2:
            matrix[i][j] = '*'

for x in range(n):
    print(*matrix[x])


# Магический квадрат
n = int(input())

matrix = []
flag = True
for _ in range(n):
    array = [int(i) for i in input().split()]
    matrix.append(array)

digits = [i for i in range(1, n ** 2 + 1)]

d1, d2 = 0, 0
for i in range(n):
    row, col = 0, 0
    for j in range(n):
        col += matrix[j][i]
        row += matrix[i][j]
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    d1 += matrix[i][i]
    d2 += matrix[i][n - i - 1]
    if col != row:
        break

if col == row == d1 == d2 and digits == []:
    print('YES')
else:
    print('NO')
