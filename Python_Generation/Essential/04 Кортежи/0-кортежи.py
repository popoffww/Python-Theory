# Создание кортежа
city_name = input()
city_year = int(input())

city = (city_name, city_year)
print(city)

# При создании кортежа строка разбивается на отдельные символы
data = 'Python для продвинутых!'
tuple_str = tuple(data)
print(tuple_str)

# Изменение кортежа
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

data = list(poet_data)
data[2] = 'Москва'
poet_data = tuple(data)

print(poet_data)


# Увеличение кортежа
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)

print((numbers1 * 2) + (numbers2 * 9) + numbers3)


# Минимум, максимум, сумма
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
minimum = min(numbers)
maximum = max(numbers)
print((minimum + maximum))


# Непустые кортежи
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i) != 0]

print(non_empty_tuples)

# Замена последнего элемента каждого кортежа в списке на 100
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]

print(new_tuples)

# Исправление синтаксической ошибки
s = 'симпотичный'
print(s)

a = list(s)
a[4] = 'а'
s = ''.join(a)
print(s)

