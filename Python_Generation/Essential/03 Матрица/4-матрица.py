# Сложение матриц
n, m = [int(i) for i in input().split()]

matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
p = input()
matrix_2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_3 = [[int(i) for i in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

for i in range(n):
    print(*matrix_3[i])
# или
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrixC:
    print(*row)


# Умножение матриц
n, m = [int(i) for i in input().split()]

matrix_1 = [[int(i) for i in input().split()] for j in range(n)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix_2 = [[int(i) for i in input().split()] for j in range(n2)]
matrix_3 = [[0] * m2 for _ in range(n)]

for i in range(n):
    for j in range(m2):
        for k in range(m):
            matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]

for x in matrix_3:
    print(*x)


# Возведение матрицы в степень
n = int(input())

matrix_1 = [[int(i) for i in input().split()] for j in range(n)]
matrix_2 = matrix_1

x = int(input())
for _ in range(x - 1):
    matrix = [[0] * n for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    matrix_1 = matrix

for x in matrix:
    print(*x)