# Напишите программу, которая печатает таблицу размером n×3, состоящую из данного числа
number = int(input())
for i in range(number):
    print(number, number, number)


number = int(input())
for i in range(number):
    print(str(number) * 3)


number = int(input())
for i in range(number):
    for j in range(3):
        print(number, end=" ")
    print()


# Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом)
number = int(input())

for i in range(number):
    for j in range(5):
        print(i + 1, end=" ")
    print()


# Напишите программу, которая печатает таблицу сложения для всех чисел
# от 1 до n (включительно)
number = int(input())

for i in range(1, number + 1):
    for j in range(1, 10):
        print(i, "+", j, "=", i + j)
    print()



# Напишите программу, которая печатает равнобедренный звездный треугольник
# с основанием, равным n
number = int(input())

for i in range(1, number // 2 + 2):
    print('*' * i)

for j in range(number // 2, 0, -1):
    print('*' * j)


# Напишите программу, которая печатает численный треугольник
number = int(input())

for i in range(number):
    for j in range(i + 1):
        print(i + 1, end='')
    print()



# Решите уравнение в натуральных числах 28*n + 30*k + 31*m = 365
total = 0
# 365 / 28 = 13.035714285714286
for n in range(1, 14):
# 365 / 30 = 12.166666666666666
    for k in range(1, 13):
# 365 / 31 = 11.774193548387096
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print('n =', n, 'k =', k, 'm', m)
print('Общее количество натуральных решений =',  total,sep='\n',)


# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля
# и надо купить 100 голов скота?
for B in range(1, 11):
    for K in range(1, 21):
        for T in range(1, 200):
            if B*10 + K*5 + T*0.5 == 100:
                if B + K + T == 100:
                    print(B, K, T)


# Гипотеза Эйлера о сумме степеней
a = [i ** 5 for i in range(1, 151)]
b = {}
c = {}
for i in range(150):
    for j in range(i, 150):
        c.setdefault(a[j] - a[i], []).append([j + 1, i + 1])
        for k in range(j, 150):
            b.setdefault(a[i] + a[j] + a[k], []).append([k + 1, j + 1, i + 1])

lst = sorted(set(b.keys()) & set(c.keys()))
res = sum(sum(c[lst[0]] + b[lst[0]], []))
print(res)