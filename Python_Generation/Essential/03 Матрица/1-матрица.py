# След заданной квадратной матрицы - сумма элементов главной диагонали
number = int(input())

matrix = []
# создание списков в одну строку
for i in range(number):
    array = [int(j) for j in input().split()]
    # для строк без пробела
    # array = [int(j) for j in input()]
    matrix.append(array)

total = 0
# проход по спискам
for row in range(number):
    for col in range(number):
        if row == col:
            total += matrix[row][col]

print(total)

# Больше среднего
number = int(input())

matrix = []
for _ in range(number):
    array = [int(i) for i in input().split()]
    matrix.append(array)

for i in range(number):
    total = 0
    count = 0
    for j in range(number):
        total += matrix[i][j]
    for k in range(number):
        if matrix[i][k] > total / number:
            count += 1

    print(count)


# Максимальный в области 1
number = int(input())

matrix = []
for _ in range(number):
    array = [int(i) for i in input().split()]
    matrix.append(array)

maximum = matrix[0][0]

for i in range(number):
    for j in range(number):
        if i >= j and matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)

# Максимальный в области 2
number = int(input())

matrix = []
for _ in range(number):
    array = [int(i) for i in input().split()]
    matrix.append(array)

maximum = matrix[0][0]

for i in range(number):
    for j in range(number):
        if (i >= j and i <= number - 1 - j or
            i <= j and i >= number - 1 - j) and \
                matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)

# Суммы четвертей
number = int(input())

matrix = []
for _ in range(number):
    array = [int(i) for i in input().split()]
    matrix.append(array)

total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0

for i in range(number):
    for j in range(number):
        if i < j and i < number - 1 - j:
            total_1 += matrix[i][j]
        elif i < j and i > number - 1 - j:
            total_2 += matrix[i][j]
        elif i > j and i > number - 1 - j:
            total_3 += matrix[i][j]
        elif i > j and i < number - 1 - j:
            total_4 += matrix[i][j]

print('Верхняя четверть:', total_1)
print('Правая четверть:', total_2)
print('Нижняя четверть:', total_3)
print('Левая четверть:', total_4)