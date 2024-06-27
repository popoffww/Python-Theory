import math
# Миним. и максим. значение среднего арифметического кортежа
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

def average(numbers):
    return sum(numbers) / len(numbers)

print(min(numbers, key=average))
print(max(numbers, key=average))

# Сортировка
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def sorted_points(points):
    return (points[0] ** 2 + points[1] ** 2) ** 0.5

points.sort(key=sorted_points)
print(points)

# Сумма
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

def sum_min_max(numbers):
    return min(numbers) + max(numbers)

numbers.sort(key=sum_min_max)
print(numbers)


# Сортируй как хочешь
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def name(n):
    return n[0]

def age(n):
    return n[1]

def height(n):
    return n[2]

def weight(n):
    return n[3]

dct = {1: name, 2: age, 3: height, 4: weight}

n = int(input())

lst = sorted(athletes, key=dct[n])

for i in lst:
    print(*i)


# Математические функции
def operand(m):
    def number(n):
        return n ** m
    return number

dct = {'квадрат': operand(2), 'куб': operand(3), 'корень': operand(0.5), 'модуль': abs, 'синус': math.sin}

n = int(input())
operation = input()

print(dct[operation](n))

# проще
def func(x, operation):
    s = {'квадрат': x**2, 'куб': x**3, 'корень': math.sqrt(x), 'модуль': abs(x), 'синус': math.sin(x)}
    return s[operation]

x, operation = int(input()), input()
print(func(x,operation))


# Интересная сортировка-1
def total(n):
    return sum(int(i) for i in str(n))

number = [int(i) for i in input().split()]

print(*sorted(number, key=total))


# Интересная сортировка-2
def total(n):
    return sum(int(i) for i in str(n))

number = sorted(int(i) for i in input().split())

print(*sorted(number, key=total))