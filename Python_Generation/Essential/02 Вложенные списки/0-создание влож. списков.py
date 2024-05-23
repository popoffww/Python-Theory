# Создание вложенных списков с одним элементом
n = int(input())
m = int(input())
# 1 способ
array_1 = []
for _ in range(n):
    array_1.append([5] * m)
# 2 способ
array_2 = [5] * n
for j in range(n):
    array_2[j] = [5] * m
# 3 способ
array_3 = [[5] * m for k in range(n)]

print(array_1, array_2, array_3, sep='\n')

# Создание вложенных списков с многими элементами: 4 списка
# 2 4
# 6 7 8 9
# 1 3
# 5 6 5 4 3 1
n = int(input()) # n = 4
array_1 = []
array_2 = []
for _ in range(n):
    elem = [int(i) for i in input().split()]
    array_1.append(elem)
    array_2.extend(elem)
print(array_1, array_2, sep='\n')

# Перебор и вывод элементов вложенного списка
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')
    print()
print('=' * 5)
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')
    print()

# Сумма
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]

print(total)

total = 0
for row in my_list:
    for elem in row:
        total += elem

print(total)

total = 0
for row in my_list:
    total += sum(row)
print(total)