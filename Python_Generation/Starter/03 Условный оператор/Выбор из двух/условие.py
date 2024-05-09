# Напишите программу, которая проверяет,
# что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

number = int(input())
num_4 = number % 10
num_1 = (number // 1000) % 10
sum = num_1 + num_4
num_3 = (number // 10) % 10
num_2 = (number // 100) % 10
rest = num_2 - num_3
if sum == rest:
    print('ДА')
else:
    print('НЕТ')
    
    
    
number = input()
if (int(number[0]) + int(number[3])) == (int(number[1]) - int(number[2])):
    print('ДА')
else:
    print('НЕТ')


age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')


print('Доступ запрещен' if int(input()) < 18 else 'Доступ разрешен')
print(f"{('Не п', 'П')[-1 < int(input()) < 17]}ринадлежит")
if int(input()) <= 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")


# Напишите программу, которая определяет наименьшее из четырёх чисел.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
z = 0
x = 0
if a < b:
    z = a
else:
    z = b
if c < d:
    x = c
else:
    x = d
if z < x:
    print(z)
else:
    print(x)


# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел
a = int(input())
b = int(input())
c = int(input())
if a  > 0:
    a = a
else:
    a = 0

if b  > 0:
    b = b
else:
    b = 0

if c  > 0:
    c = c
else:
    c = 0

print(a + b + c)





