# Середина отрезка
def get_middle_point(x1, y1, x2, y2):

    return (x1 + x2) / 2, (y1 + y2) / 2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)



# Площадь и длина круга
from math import pi

def get_circle(radius):

    length = 2 * pi * radius
    square = pi * (radius ** 2)

    return length, square

r = float(input())

length, square = get_circle(r)
print(length, square)


# Корни уравнения(решение 6.3 Модуль math)
from math import sqrt, pow

def solve(a, b, c):
    # Дискриминант
    D = pow(b, 2) - 4 * (a * c)

    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)

    if D == 0:
        return x1, x2
    else:
        if x1 >= x2:
            return x2, x1
        else:
            return x1, x2

a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)


# 6.3 Модуль math
a = float(input())
b = float(input())
c = float(input())

# Дискриминант
D = pow(b, 2) - 4 * (a * c)

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif D == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')