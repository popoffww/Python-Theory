import math

number = int(input())
factorial = None
for i in range(1, number + 1):
    factorial = math.factorial(i)
print(factorial)


factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)


res = 1
i = 2
while i <= number:
    res *= i
    i += 1
print(res)

# Сумма факториалов
total = 1
x = 0

for i in range(1, number + 1):
    for j in range(1, i + 1):
        total *= j
    x += total
    total = 1
print(x)