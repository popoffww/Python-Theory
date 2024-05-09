# Напишем программу, определяющую, что натуральное число является простым
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

# Усовершенствуем с помощью оператора break программу, проверяющую число на простоту
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag:  # эквивалентно if flag == True:
    print('Число простое')
else:
    print('Число составное')


# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b (включительно),
# куб которых оканчивается на 4 или 9
a = int(input())
b = int(input())
counter = 0
for i in range(a, b+1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        counter = counter + 1
print(counter)

# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел (не включая само число n)
_range = int(input())
total = 0

for _ in range(_range):
    number = int(input())
    total = total + number
print(total)

# Асимптотическое приближение
from math import log

number = int(input())
total = 0
for i in range(1, number + 1):
    total = total + (1 / i)
print(total - log(number))

# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно),
# квадрат которых оканчивается на 2,5 или 8
number = int(input())
counter = 0
for i in range(1, number + 1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        counter += i
print(counter)


number = int(input())
total = 0
for i in range(1, number + 1):
    if i ** 2 % 10 in [2, 5, 8]:
        total += i
print(total)

# Так как не существует чисел, квадрат которых оканчивается на 2 и на 8, то не смотрим вообще этот случай.
# Квадрат числа оканчивается на 5, если само число оканчивается на 5,
# тогда и будем смотреть только такие числа: 5, 15, 25
number = int(input())
total = 0
for i in range(5, number + 1, 10):
    total += i
print(total)

# Факториал
number = int(input())
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)

import math
number = int(input())
factorial = None
for i in range(1, number + 1):
    factorial = math.factorial(i)
print(factorial)

# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел
multi = 1
for i in range(1, 11):
    number = int(input())
    if number != 0:
        multi *= number
print(multi)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей
number = int(input())
total = 0
for i in range(1, number + 1):
    if number % i == 0:
        total += i
print(total)

# Знакочередующаяся сумма
number = int(input())
total = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)

# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел последовательности, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности
_range = int(input())

# значение -1 для того, чтобы впоследствии
# присвоить переменным max_1 и max_2 значения натуральных чисел
# в переменной - number = int(input())
max_1, max_2 = -1, -1

for i in range(_range):
    number = int(input())
    if number > max_1:

# чтобы не потерять ранее присвоенное значение max_1 на предыдущей итерации,
# присваиваем max_2 новое значение max_1
        max_1, max_2 = number, max_1

    elif number > max_2:
        max_2 = number

print(max_1, max_2, sep='\n')

# Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет, является ли каждое из них четным или нет
flag = True
for i in range(10):
    number = int(input())
    if number % 2 != 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')

# Последовательность Фибоначчи
number = int(input())

x1, x2 = 1, 1
for i in range(number):
    print(x1, end=' ')
    x1, x2 = x2, x1 + x2