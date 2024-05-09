# Напишите программу, которая выводит его цифры в столбик в обратном порядке
number = int(input())
while number != 0:
    last = number % 10
    number = number // 10
    print(last, sep='\n')

# Напишите программу, которая меняет порядок цифр числа на обратный и выводит их в строку
number = int(input())
while number != 0:
    last = number % 10
    number = number // 10
    print(last, end='')

# Напишите программу, которая определяет его максимальную и минимальную цифры
number = int(input())
maximum = 0
minimum = 9
while number != 0:
    last = number % 10
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last

    number = number // 10
print("Максимальная цифра равна", maximum)
print("Минимальная цифра равна", minimum)

# Арифметика
number = int(input())
total = 0
counter = 0
multi = 1
average = 0
start = number % 10
summary = 0
while number != 0:
    last = number % 10
    number = number // 10

    total += last
    counter += 1
    multi *= last
    average = total / counter
    summary = last + start
print(total, counter, multi, average, last, summary, sep='\n')

# Напишите программу, которая определяет его вторую (с начала) цифру
number = int(input())
while number >= 10:
    result = number % 10
    number //= 10
print(result)

# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр
number = int(input())
last_1 = number % 10
flag = True

while number != 0:
    last_2 = number % 10
    if last_2 != last_1:
        flag = False
        break
    number //= 10

if flag:
    print('YES')
else:
    print('NO')

# Напишите программу, которая определяет, является ли последовательность его цифр
# при просмотре справа налево упорядоченной по неубыванию
number = int(input())
flag = True

while number >= 10:
    last_1 = number % 10
    last_2 = number % 100 // 10
    if last_1 > last_2:
        flag = False
        break
    number //= 10

if flag:
    print('YES')
else:
    print('NO')


# Напишите программу, которая выводит его наименьший отличный от 1 делитель
number = int(input())
for i in range(2, number + 1):
    if number % i == 0:
        print(i)
        break

# Напишите программу, которая выводит числа от 1 до n включительно за исключением:
number = int(input())
for i in range(1, number + 1):
    if i in range(5, 10):
        continue
    elif i in range(17, 38):
        continue
    elif i in range(78, 88):
        continue
    print(i)