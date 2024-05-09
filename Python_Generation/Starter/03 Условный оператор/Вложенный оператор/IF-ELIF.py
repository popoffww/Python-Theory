# Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.
side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

if side_1 == side_2 == side_3:
    print('Равносторонний')
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print('Равнобедренный')
else:
    print('Разносторонний')


month = int(input())
if month == 2:
    print('28')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30')
else:
    print('31')

# Среднее число
a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)

# Калькулятор
number_1 = int(input())
number_2 = int(input())
sign = input()

if sign == '+':
    print(number_1 + number_2)
elif sign == '-':
    print(number_1 - number_2)
elif sign == '*':
    print(number_1 * number_2)
elif sign == '/':
    if number_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(number_1 / number_2)
else:
    print('Неверная операция')


# Цвета
color_1 = str(input())
color_2 = str(input())

red = 'красный'
blue = 'синий'
yellow = 'желтый'
violet = 'фиолетовый'
orange = 'оранжевый'
green = 'зеленый'

if (color_1 == red and color_2 == blue) or (color_2 == red and color_1 == blue):
    print(violet)
elif (color_1 == red and color_2 == yellow) or (color_2 == red and color_1 == yellow):
    print(orange)
elif (color_1 == blue and color_2 == yellow) or (color_2 == blue and color_1 == yellow):
    print(green)
elif (color_1 == red or color_1 == blue or color_1 == yellow) and (color_1 == color_2):
    print(color_1)
else:
    print('ошибка цвета')


# Рулетка
number = int(input())

if number == 0:
    print('зеленый')
elif 1 <= number <= 10:
    if number % 2 != 0:
        print('красный')
    else:
        print('черный')
elif 11 <= number <= 18:
    if number % 2 != 0:
        print('черный')
    else:
        print('красный')
elif 19 <= number <= 28:
    if number % 2 != 0:
        print('красный')
    else:
        print('черный')
elif 29 <= number <= 36:
    if number % 2 != 0:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')


number = int(input())

if -1 < number < 37:
    if number == 0:
        print('зеленый')
    elif 0 < number < 11 or 18 < number < 29:
        if number != 0:
            print('красный')
        else:
            print('черный')
    elif number != 0:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')


# Пересечение отрезков
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')




