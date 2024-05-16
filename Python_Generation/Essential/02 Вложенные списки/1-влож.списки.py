# Reverse списки
list1 = [[1, 8, 7, 4], [1, 3, 4, 5], [2, 7, 2], [2, 6, 7, 8]]
list1.reverse()
print(list1)

# Reverse элементы
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for li in range(len(list1)):
    list1[li].reverse()
print(list1)

# Сумма / количество элементов
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for li in range(len(list1)):
    total += sum(list1[li])
    counter += len(list1[li])

print(total / counter)

# Расширить список
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']

list1[2][1][2].extend(['h', 'i', 'j'])
print(list1)
list1[2][1].extend(['h', 'i', 'j'])
print(list1)
print(len(list1))


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


# Максимум
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = list1[2][1]
print(maximum)