# Произведение элементов
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)

multi = 1

for i in range(len(numbers)):
    multi *= numbers[i]
print(multi)


# Средние арифметические значения чисел каждого вложенного кортежа
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

total = 0
average = 0
array = []

for i in range(len(numbers)):
    total = sum(numbers[i])
    average = total / len(numbers[i])
    array.append(average)

print(array)


# Вершина параболы
def top_of_parabola(a, b, c):

    x = -b / (2 * a)
    y = (4 * a * c - b ** 2) / (4 * a)

    return x, y

a, b, c = int(input()), int(input()), int(input())
print(top_of_parabola(a, b, c))

# Другой вариант
a, b, c = [int(input()) for _ in range(3)]
x0 = -b / (2 * a)
y0 = (4 * a * c - b**2) / (4 * a)
vertex = (x0, y0)

print(vertex)


# Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке.
# Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке)
tpl = [tuple(input().split()) for _ in range(int(input()))]

for c in tpl:
    print(*c)
print()

for c in tpl:
    if int(c[1]) >= 4:
        print(*c)

# Изящное решение
students = [tuple(input().split()) for _ in range(int(input()))]

for student in students:
    print(*student)
print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)


# Трибоначчи
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3

print()

# Фибоначчи
n = int(input())
f1, f2 = 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2