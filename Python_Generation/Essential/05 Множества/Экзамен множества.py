# (параметры | ЕГЭ) & математика = 430

# Домашнее задание
# Учитель проверяет домашнее задание в классе и получил следующие ответы:
# из n школьников у m домашнее задание съела собака, у k отключили свет, а у
# p учеников постигли оба несчастья.
# Напишите программу, которая определяет сколько человек выполнило домашнее задание
n, m, k, p = int(input()), int(input()), int(input()), int(input())
a = m - p
b = k - p

print(n - a - b - p)


# Восход
# Максимальное количество показаний,
# после удаления которых анализ результатов будет произведен верно
sunrise = input().split()
print(len(sunrise) - len(set(sunrise)))


# Повтор города
n = int(input())

city = [input() for _ in range(n + 1)]
if len(city) == len(set(city)):
    print('OK')
else:
    print('REPEAT')
# или
n = int(input())
towns = {input() for _ in range(n)}
town = input()

if town in towns:
    print('REPEAT')
else:
    print('OK')


# Книги на прочтение
m, n = int(input()), int(input())

books = {input() for _ in range(m)}

for _ in range(n):
    if input() in books:
        print('YES')
    else:
        print('NO')


# Странное увлечение
# Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке,
# либо словосочетание BAD DAY, если таких чисел нет
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())

if a & b:
    print(*sorted(a & b, reverse=True))
else:
    print('BAD DAY')
# или
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

if set1.isdisjoint(set2):
    print('BAD DAY')
else:
    print(*sorted(set1 & set2, reverse=True))


# Онлайн-школа BEEGEEK 1
# Без лишних чисел
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())

if a.issubset(b) and b.issubset(a):
    print('YES')
else:
    print('NO')
# или
set1 = set(input().split())
set2 = set(input().split())

res = ("NO", "YES")[set1 == set2]
print(res)

# Онлайн-школа BEEGEEK 2
m = int(input())
n = int(input())

a = {input() for _ in range(m)}
b = {input() for _ in range(n)}

print(m - (len(a & b)))
# или
m, n = [int(input()) for _ in range(2)]

math = {input() for _ in range(m)}
informatics = {input() for _ in range(n)}

only_math = math - informatics
print(len(only_math))


# Онлайн-школа BEEGEEK 3
m = int(input())
n = int(input())

a = {input() for _ in range(m)}
b = {input() for _ in range(n)}

if len(a - b) + len(b - a) != 0:
    print(len(a - b) + len(b - a))
else:
    print('NO')
# или
m, n = int(input()), int(input())
math = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
result = len(math ^ inf)

if result:
    print(result)
else:
    print('NO')


# Онлайн-школа BEEGEEK 4
# Все фамилии
a = set(input().split())
b = set(input().split())

print(*sorted(a | b))


# Онлайн-школа BEEGEEK 5
m, n = [int(input()) for _ in range(2)]

# список студентов (в том числе с повторами)
students_list = [input() for _ in range(m + n)]
# множество студентов (уже без повторов)
students_set = set(students_list)

# изучающие сразу два предмета
both_subjects = len(students_list) - len(students_set)
# изучающие только один предмет
only_one_subject = len(students_set) - both_subjects

print(only_one_subject or "NO")
# или
m, n = int(input()), int(input())

stud_lst = [input() for _ in range(m + n)]
stud_set = set(stud_lst)
less = len(stud_lst) - len(stud_set)

if len(stud_set) - less == 0:
    print('NO')
else:
    print(len(stud_set) - less)


# Онлайн-школа BEEGEEK 6
n = int(input())

result = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))}

print(*sorted(result), sep='\n')