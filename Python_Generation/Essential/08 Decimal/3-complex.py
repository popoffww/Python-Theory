# Математика
n, m = input(), input()

z1 = complex(n)
z2 = complex(m)

print(f'{z1} + {z2} =', z1 + z2)
print(f'{z1} - {z2} =', z1 - z2)
print(f'{z1} * {z2} =', z1 * z2)


# Комплексное число с наибольшим модулем и сам модуль числа
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

num = 0
for el in numbers:
    if abs(el) > abs(num):
        num = el
print(num, abs(num), sep='\n')


# Сопряженные числа
n = int(input())
z1, z2 = complex(input()), complex(input())

print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))