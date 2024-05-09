# Звездный прямоугольник с размерами 14×10
def draw_box():
    print("*" * 10)

    for i in range(12):
        print("*", "*", sep=" " * 8)

    print("*" * 10)

draw_box()

# Второй вариант
def draw_box():
    for i in range(1, 15):
        if i == 1 or i == 14:
            print('*' * 10)
        else:
            print("*", "*", sep=" " * 8)

draw_box()

# Звездный прямоугольник с катетами, равными 10
def draw_box():
    for i in range(10):
        for j in range(i + 1):
            print('*', end='')
        print()

draw_box()


# Звездный треугольник
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)

    for j in range(base // 2, 0, -1):
        print(fill * j)

fill = input()
base = int(input())
draw_triangle(fill, base)


# ФИО
def print_fio(name, surname, patronymic):
    print(surname[0].upper() + name[0].upper() + patronymic[0].upper())

name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)



# Сумма цифр
def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    print(sum)

n = int(input())
print_digit_sum(n)
