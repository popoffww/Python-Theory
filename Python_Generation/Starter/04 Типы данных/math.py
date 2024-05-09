# Евклидово расстояние
from math import sqrt, pow
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
pow = pow((x1 - x2), 2) + pow((y1 - y2), 2)
E = sqrt(pow)
print(E)

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R
import math
radius = float(input())
S = math.pi * pow(radius, 2)
C = (math.pi * 2) * radius
print(S, C, sep='\n')

# Средние значения
from math import sqrt, pow
a = float(input())
b = float(input())
# среднее арифметическое
avr_1= (a + b) / 2
# среднее геометрическое
avr_2 = sqrt(a * b)
# среднее гармоническое
avr_3 = 2 * (a * b) / (a + b)
# среднее квадратичное
avr_4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(avr_1, avr_2, avr_3, avr_4, sep='\n')

# Напишите программу, вычисляющую значение тригонометрического выражения
from math import radians, sin, cos, tan, pow
number = float(input())
# тригонометрические функции принимают аргумент в радианах
radian = radians(number)
sinus = sin(radian)
cosinus = cos(radian)
tangens = tan(radian)
result = pow(tangens, 2) + sinus + cosinus
print(result)

# Пол и потолок
from math import ceil, floor
number = float(input())
top = ceil(number)
down = floor(number)
result = top + down
print(result)

# Квадратное уравнение
from math import sqrt, pow
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

# Правильный многоугольник
import math
from math import tan, pow
n = float(input())
a = float(input())
res_1 = pow(a, 2) * n
res_2 = 4 * tan(math.pi / n) # pi / n - это значение уже и есть радианы
S = res_1 / res_2
print(S)