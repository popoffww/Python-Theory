# Именованные аргументы
def matrix(n=1, m=None, value=0):
    if m == None:
        m = n

    matrix = [[value] * m for _ in range(n)]
    return matrix

x, y = int(input()), int(input())

print(matrix())          # матрица 1 × 1 из 0
print(matrix(3))         # матрица 3 × 3 из 0
print(matrix(2, 5))      # матрица 2 × 5 из 0
print(matrix(3, 4, 9))   # матрица 3 × 4 из 9

# Переменные аргументы
# Количество переданных аргументов
def count_args(*args):
    return len(args)

print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))


# Сумма квадратов
def sq_sum(*args):
    return sum([i ** 2 for i in args])

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Среднее арифметическое int или float аргументов
def mean(*args):
    s = ([i for i in args if type(i) in (int, float)])
    if len(s) == 0:
        return 0.0
    return sum(s) / len(s)

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Приветствие
def greet(name, *args):
    s = ' and '.join((name,) + args)
    return f'Hello, {s}!'

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))

# Список продуктов
def print_products(*args):
    s = [i for i in args if type(i) == str and len(i) > 1]
    if len(s) == 0:
        print('Нет продуктов')
    else:
        for i in range(1, len(s) + 1):
            print(f'{i}) {s[i - 1]}')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')


# Словарь
def info_kwargs(**kwargs):
    # 1-й вывод
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')

    # 2-й вывод
    print(kwargs)

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')