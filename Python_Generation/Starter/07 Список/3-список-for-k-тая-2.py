# Сумма квадратов списка
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for _ in range(len(numbers)):
    total += numbers[_] ** 2
print(total)

# Напишите программу, которая для каждого введенного числа x выводит значение функции
# f(x) = x ** 2 + 2 * x + 1, каждое на отдельной строке
_range = int(input())
array = []
array_2 = []
counter = 0

for _ in range(_range):
    array.append(int(input()))

print(*array, sep='\n')
print()

for c in array:
    print(c **2 + c * 2 + 1)


# Удалить самое большое и самое маленькое значение
_range = int(input())
array = []
array_2 = []
for i in range(_range):
    number = int(input())
    array.append(number)
for i in array:
    if i != min(array) and i != max(array):
        array_2.append(i)
print(*(array_2), sep='\n')

# Второй вариант
_range = int(input())
array = []
for i in range(_range):
    number = int(input())
    array.append(number)
del array[array.index(max(array))]
del array[array.index(min(array))]
# array.remove(max(array))
# array.remove(min(array))

print(*array, sep='\n')


# Без дубликатов
_range = int(input())
array = []
for i in range(_range):
    string = input()
    if string not in array:
        array.append(string)

print(*array, sep='\n')

# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос
_range = int(input())
array = []

for _ in range(_range):
    array.append(input())
search = input()
for i in range(len(array)):
    if search.lower() in array[i].lower():
        print(array[i])


# Корявое решение с учетом регистра
_range = int(input())
array = []
array_2 = []
for i in range(1, _range + 2):
    string = input()
    array.append(string)
for i in array:
    if array[-1] in i:
        array_2.append(i)
        del array[-1]

print(*array_2, sep='\n')

# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы
_range = int(input())
array = []
array_2 = []
counter = 0

for _ in range(_range):
    array.append(input())

search = int(input())
for _ in range(search):
    array_2.append(input())

for i in range(_range):
    for j in range(search):
        if array_2[j].lower() in array[i].lower():
            counter += 1
    if counter == search:
        print(array[i])
    counter = 0


# Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
# а затем все положительные числа, каждое на отдельной строке
_range = int(input())
negative = []
zero = []
positive = []
for i in range(_range):
    number = int(input())
    if number < 0:
        negative.append(number)
    elif number == 0:
        zero.append(number)
    elif number > 0:
        positive.append(number)

print(*(negative), *(zero), *(positive), sep='\n')