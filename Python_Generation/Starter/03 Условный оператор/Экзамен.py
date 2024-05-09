# Начало столетия
number = int(input())
if (number % 10) == 0 and (number // 10) % 10 == 0:
    print('YES')
else:
    print('NO')


# Шахматная доска
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')



# Girls only
age = int(input())
sex = input()
if (10 <= age <= 15) and sex == 'f':
    print('YES')
elif (10 <= age <= 15) and sex == 'm':
        print('NO')
else:
    print('NO')



number = int(input())
if 0 < number < 11:
    if number == 1:
        print('I')
    if number == 2:
        print('II')
    if number == 3:
        print('III')
    if number == 4:
        print('IV')
    if number == 5:
        print('V')
    if number == 6:
        print('VI')
    if number == 7:
        print('VII')
    if number == 8:
        print('VIII')
    if number == 9:
        print('IX')
    if number == 10:
        print('X')
else:
    print('ошибка')




number = int(input())
if number % 2 != 0:
    print('YES')
elif (2 <= number <= 5) and number % 2 == 0:
    print('NO')
elif (6 <= number <= 20) and number % 2 == 0:
    print('YES')
elif number > 20 and number % 2 == 0:
    print('NO')


# Ход слона
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')


# Ход коня
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

# Ход ферзя
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
