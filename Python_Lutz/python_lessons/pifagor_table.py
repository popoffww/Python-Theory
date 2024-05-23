# Таблица умножения
for i in range(1,11,1):
    for j in range(1,11,1):
        print(i * j, end = '|')
    print()



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