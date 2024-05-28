# Сумма квадратов элементов множества
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}

square_sum = 0
for el in numbers:
    square_sum += el ** 2

print(square_sum)

# Обратная сортировка множества
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

sorted_fruits = sorted(fruits, reverse=True)

print(*sorted_fruits, sep='\n')


# Количество символов без пробелов
s = input()
print(len(set(s)))


# Определить, что в строке ни одна из цифр не повторяется
string = input()

if len(set(string)) == len(string):
    print('YES')
else:
    print('NO')


# Все 10 цифр
s = input() + input()

if len(set(s)) == 10:
    print("YES")
else:
    print("NO")


# Одинаковые наборы цифр
string_1 = input()
string_2 = input()

if set(string_1) == set(string_2):
    print('YES')
else:
    print('NO')

# или
a, b = [set(input()) for _ in range(2)]

if a == b:
    print("YES")
else:
    print("NO")


# Верно ли, что для записи всех трех слов был использован один и тот же набор букв
string = input().split()

set_1 = set(string[0])
set_2 = set(string[1])
set_3 = set(string[2])

if set_1 == set_2 == set_3:
    print('YES')
else:
    print('NO')

# или
a, b, c = [set(el) for el in input().split()]

if a == b == c:
    print("YES")
else:
    print("NO")