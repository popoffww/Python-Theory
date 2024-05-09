# Напишите программу, которая создает из указанных строк список и выводит его
number = int(input())
array = []
for i in range(number):
    string = input()
    array.append(string)
print(array)

# Символы всех строк
_range = int(input())
array = []
for _ in range(_range):
    string = input()
    array.extend(string)
print(array)


# Увеличение количества каждой буквы алфавита
array = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = 0
for c in alphabet:
    # создается множитель 1-26 по кол-ву букв
    counter += 1
    # произведение каждой буквы на множитель
    c *= counter
    array.append(c)
print(array) # общий вывод списка
print(counter) # выводит цифры
print(c) # выводит буквы

# Второй вариант
array = []
for i in range(1, 27):
    array.append(chr(96 + i) * i)

    print(array)


# Напишите программу, которая создает из указанных чисел список их кубов
_range = int(input())
array = []
for i in range(_range):
    number = int(input())
    value = number ** 3
    array.append(value)

print(array)


# Напишите программу, которая создает список, состоящий из делителей введенного числа
number = int(input())
array = []
for i in range(1, number + 1):
    if number % i == 0:
        array.append(i)

print(array)


# Нечетные индексы
_range = int(input())
array = []
for _ in range(_range):
    number = int(input())
    array.append(number)

print(array[::2])


# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел
_range = int(input())
array = []
value = 0
for i in range(_range):
    number = int(input())
    value += number
    array.append(value)
    value = number

print(array[1:])


# На вход программе подается натуральное число n и nn строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов
_range = int(input())
array = []
result = ''

for _ in range(_range):
    array.append(input())

index = int(input())

for i in array:
    if index <= len(i):
        result += i[index - 1]
print(result)