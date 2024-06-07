# Шахматная доска
str_num = input().split()
n, m = int(str_num[0]), int(str_num[1])

matrix = []

for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = '.'
        else:
            matrix[i][j] = '*'

for i in range(n):
    print(*matrix[i])
# или
n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)


# Побочная диагональ
n = int(input())

matrix = []

for _ in range(n):
    array = [int(i) for i in range(n)]
    matrix.append(array)

for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            matrix[i][j] = 1
        elif i < n - 1 - j:
            matrix[i][j] = 0
        elif i > n - 1 - j:
            matrix[i][j] = 2

for i in range(n):
    print(*matrix[i])
# или
n = int(input())
matrix = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
# Можно изначально матрицу заполнить двойками, и тогда в цикле можно убрать блок else
        else:
            matrix[i][j] = 2

for row in matrix:
    print(*row)


# Заполнение 1
n, m = [int(i) for i in input().split()]

matrix = []

for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

count = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# Заполнение 2
n, m = [int(i) for i in input().split()]

matrix = []

for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

count = 1

for j in range(m):
    for i in range(n):
        matrix[i][j] = count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# Заполнение 3
n = int(input())

matrix = []

for _ in range(n):
    array = [0 for i in range(n)]
    matrix.append(array)

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        if i == n - 1 - j:
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            matrix[i][j] = 1

for row in matrix:
    print(*row)


# Заполнение 4
n = int(input())

matrix = []

for _ in range(n):
    array = [0 for i in range(n)]
    matrix.append(array)

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            matrix[i][j] = 1
        elif i >= j and i >= n - 1 - j:
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# Заполнение 5
n, m = [int(i) for i in input().split()]

array = [i for i in range(1, m + 1)]
matrix = []

for _ in range(n):
    matrix.append(array)
    array = array[1:] + [array[0]]


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n, m = [int(i) for i in input().split()]
numbers = list(range(1, m + 1))
matrix = []

for _ in range(n):
    matrix.append(numbers)
    # переносим первый элемент списка в конец
    numbers = numbers[1:] + [numbers[0]]

for row in matrix:
    print(*row)


# Заполнение змейкой
n, m = [int(i) for i in input().split()]

matrix = []

for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

count = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1

for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# Заполнение диагоналями
n, m = [int(i) for i in input().split()]

matrix = []

for _ in range(n):
    array = [i for i in range(m)]
    matrix.append(array)

count = 1

for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = count
                count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
# или
n, m = [int(el) for el in input().split()]
matrix = [[None for _ in range(m)] for _ in range(n)]
cnt = 1

# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()


# Заполнение спиралью
n, m = map(int, input().split())

i = 0
j = 0
cnt = 1

a = [[0 for _ in range(m)] for _ in range(n)]

while cnt < m * n:
    while j < m - 1 and a[i][j + 1] == 0:
        a[i][j] = cnt
        j += 1
        cnt += 1

    while i < n - 1 and a[i + 1][j] == 0:
        a[i][j] = cnt
        i += 1
        cnt += 1

    while j > 0 and a[i][j - 1] == 0:
        a[i][j] = cnt
        j -= 1
        cnt += 1

    while i > 0 and a[i - 1][j] == 0:
        a[i][j] = cnt
        i -= 1
        cnt += 1

a[i][j] = cnt

for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end=' ')
    print()