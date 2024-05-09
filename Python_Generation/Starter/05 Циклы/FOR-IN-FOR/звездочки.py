# Прямоугольник
for i in range(8):
    for j in range(6):
        print('*', end='')
    print()
print('=' * 10)

# Треугольник
for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()


# Звездный прямоугольник с размерами 14×10
# объявление функции
def draw_box():
    print("*" * 10)

    for i in range(12):
        print("*", "*", sep=" " * 8)

    print("*" * 10)

draw_box()  # вызов функции


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
