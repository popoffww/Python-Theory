# Factorial
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)

# Минимальный делитель числа, отличный от единицы
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)


# Ревью кода - 7: сумма четных цифр этого числа или 0
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)


# Ревью кода - 8: количество делящихся нацело на 4 чисел в исходной последовательности
# и максимальное делящееся нацело на 4 число
# вводимые числа по абсолютной величине не превышают 10 ** 12
count = 0
maximum = -10 ** 13
for i in range(8):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# Ревью кода - 9: количество нечетных чисел в исходной последовательности
# и максимальное нечетное число
# вводимые числа по абсолютной величине не превышают 10 ** 8
count = 0
maximum = -10 ** 9
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count != 0:
    print(count)
    print(maximum)
else:
    print('NO')


# Звездная рамка
n = int(input())

print("*" * 19)

for i in range(n - 2):
    print("*", "*", sep=" " * 17)

print("*" * 19)

for i in range(n):
    if i == 0 or i == n - 1:
        cur_sep = "*"
    else:
        cur_sep = " "

    print("*", "*", sep=cur_sep * 17)


# Все вместе
number = int(input())

count_3 = 0
last_digit = number % 10
count_last_digit = 0
count_even_digits = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_5 = 0

while number > 0:
    cur_digit = number % 10

    if cur_digit == 3:
        count_3 += 1
    if cur_digit == last_digit:
        count_last_digit += 1
    if cur_digit % 2 == 0:
        count_even_digits += 1
    if cur_digit > 5:
        sum_greater_than_5 += cur_digit
    if cur_digit > 7:
        product_greater_than_7 *= cur_digit
    if cur_digit == 0 or cur_digit == 5:
        count_0_5 += 1

    number //= 10

print(count_3, last_digit, count_even_digits, sum_greater_than_5,
      product_greater_than_7,count_0_5, sep='\n')


# Числа Рамануджана: 1729 = 1 ** 3 + 12 ** 3 = 9 ** 3 + 10 ** 3
a, b, c, d = 1, 12, 9, 10
s = 0
for a in range(1, 50):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    s += 1
                    if s > 5:  # для печати только 5 цифр
                        break
                    print(a ** 3 + b ** 3)