# Количество совпадающих пар
string = input().split()
array = list(string)
counter = 0
# цикл проходит от первого индекса: 0
for i in range(0, len(array) - 1):
# цикл проходит от второго индекса: 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            counter += 1
print(counter)


# Численный треугольник 1
number = int(input())
for i in range(number):
    for j in range(i + 1):
        print(i + 1, end='')
    print()


# Численный треугольник 2
number = int(input())
counter = 0
for i in range(1, number + 1):
    for j in range(i):
        counter += 1
        print(counter, end=' ')
    print()

# Численный треугольник 3
number = int(input())
for i in range(1, number + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()


# Делители 1
# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из отрезка a-b с максимальной суммой делителей и сумму его делителей.
# Если таких чисел несколько, то выведите наибольшее из них
a = int(input())
b = int(input())

total = 0
maximum = 0
number = 0

for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= maximum:
        maximum = total
        number = i
    total = 0
print(number, maximum)


# Делители 2
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа
number = int(input())
counter = 0
for i in range(1, number + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    print(str(i) + '+' * counter)
    counter = 0


# Цифровой корень
number = int(input())

while number > 9:
    total = 0
    while number != 0:
        total += number % 10
        number //= 10
    number = total
print(number)


# Сумма факториалов
number = int(input())

total = 1
x = 0

for i in range(1, number + 1):
    for j in range(1, i + 1):
        total *= j
    x += total
    total = 1
print(x)

# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно
