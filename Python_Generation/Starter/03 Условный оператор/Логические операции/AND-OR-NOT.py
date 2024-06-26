# Напишите программу, которая принимает целое число xx и определяет,
# принадлежит ли данное число указанному промежутку.
number = int(input())
if number > -1 and number < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет,
# принадлежит ли данное число указанным промежуткам.
number = int(input())
if number <= -3 or not (number < 7):
    print('Принадлежит')
else:
    print('Не принадлежит')

number = int(input())
if number <= -3 or number >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет,
# принадлежит ли данное число указанным промежуткам.
number = int(input())
if -30 > number <= -2 or 7 > number <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')


# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым.
number = int(input())
if 1000 <= number <= 9999 and (number % 7 == 0 or number % 17 == 0):
    print('Число 4-х значное и делится нацело на 7, но не на 17')
else:
    print('Число 4-х значное и НЕ делится нацело на 7, но не на 17')


# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
else:
    print('Треугольник не существует', end='(вырожденный треугольник)')


# Напишите программу, которая определяет, является ли год с данным номером високосным.
year = int(input())
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')

# Ход ладьи
col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if col_1 == col_2 or row_1 == row_2:
    print('Ладья так ходит')
else:
    print('Ладья так не ходит')


# Ход короля
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')