# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль,
# то вывести «Обратного числа не существует» (без кавычек).
number = float(input())

if number != 0:
    print(1 / number)
elif number == 0:
    print('Обратного числа не существует')

# Celcius => Fahrenheit
fahrenheit = float(input())
celcius = (5 / 9) * (fahrenheit - 32)
print(celcius)

# Собачий возраст
dog_year = int(input())
equiv = 21
dog_age = equiv + (dog_year - 2) * 4
if dog_year == 2:
    print(equiv)
elif dog_year == 1:
    print(equiv / 2)
else:
    print(dog_age)

# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.
number = float(input())
result = int(number * 10 % 10)
print(result)

# Дробная часть
number = float(input())
result = number % 1
print(result)

# Напишите программу,
# которая упорядочивает три числа от большего к меньшему
a = int(input())
b = int(input())
c = int(input())
max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = (a + b + c) - (max_num + min_num)
print(max_num, mid_num, min_num, sep='\n')

# Второй вариант: три числа от большего к меньшему
# (непонятно почему неправильный? якобы не учитывается равенство цифр?)
a = int(input())
b = int(input())
c = int(input())
max_num = max(a, b, c)
min_num = min(a, b, c)
if min_num < a < max_num:
    print(max_num)
    print(a)
    print(min_num)
elif min_num < b < max_num:
    print(max_num)
    print(b)
    print(min_num)
else:
    print(max_num)
    print(c)
    print(min_num)

# Назовем число интересным, если в нем разность максимальной и минимальной цифры
# равняется средней по величине цифре
number = int(input())
start_num = (number // 100) % 10
mid_num = (number // 10) % 10
end_num = number % 10
max_num = max(start_num, mid_num, end_num)
min_num = min(start_num, mid_num, end_num)
mid_num = (start_num + mid_num + end_num) - (max_num + min_num)
diff = max_num - min_num
if diff == mid_num:
    print('Число интересное')
else:
    print('Число неинтересное')

# Манхэттенское расстояние
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

manhattan_way = abs(p1 -q1) + abs(p2 - q2)
print(manhattan_way)