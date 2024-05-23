# Вывести матрицу
_row = int(input())
_col = int(input())

matrix = []

for _ in range(_row):
    array = []
    for _ in range(_col):
        array.append(input())
    matrix.append(array)
print(matrix)

print('=' * 20)
# Перебор матрицы по строкам
for row in range(_row):
    for col in range(_col):
        print(matrix[row][col], end=' ')
    print()

print()
# Перебор матрицы по столбцам
for col in range(_col):
    for row in range(_row):
        print(matrix[row][col], end=' ')
    print()

# Короткое решение
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)

# Еще вариант
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# Квадратная матрица
number = int(input())
# 1. Списочное выражение
matrix_1 = [input() for _ in range(number)]
for row in matrix_1:
    print(*row)
# 2. Цикл
matrix_2 = []
for _ in range(number):
    matrix_2.append(input())

for row in matrix_2:
    print(*row)