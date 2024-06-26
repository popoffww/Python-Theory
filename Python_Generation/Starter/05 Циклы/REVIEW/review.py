# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение
count = 0
multi = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        multi *= x
        count += 1
if count > 0:
    print(count)
    print(multi)
else:
    print('NO')


# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Известно, что вводимые числа по абсолютной величине не превышают 10**6.
# Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и
# максимальное отрицательное число в последовательности
mx = -10 ** 6
sum = 0
for i in range(10):
    x = int(input())
    if x < 0:
        sum += x
    if x < 0 and x > mx:
        mx = x
if sum < 0:
    print(sum)
    print(mx)
else:
    print('NO')

# На обработку поступает последовательность из 7 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности или 0,
# если чётных чисел в последовательности нет
sum = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        sum += n
print(sum)

# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3.
# Если в числе нет цифр, кратных 3, требуется на экран вывести «NO»
n = int(input())

max_digit = -1
while n != 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n //= 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)


# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру
n = int(input())
while n >= 10:
    last = n % 10
    n //= 10
print(n)


# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа
n = int(input())
product = 1
while n != 0: # while n > 0
    digit = n % 10
    n //= 10
    product = product * digit
print(product)