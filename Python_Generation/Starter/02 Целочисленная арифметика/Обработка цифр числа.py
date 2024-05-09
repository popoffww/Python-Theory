# 5 % 9 = 5, 3 % 13 = 3

# print(5 // 2)  # 2
# print(-5 // 2)  # -3


# Напишите программу, определяющую число десятков и единиц в двузначном числе.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Число десятков =', first_digit)
print('Число единиц =', last_digit)

# Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Сумма цифр =', last_digit + first_digit)

# Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Искомое число =', last_digit * 10 + first_digit)

# Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую).
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(digit1, digit2, digit3, sep=',')




