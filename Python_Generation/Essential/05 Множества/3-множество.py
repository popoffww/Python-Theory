# Количество чисел, которые есть как в первой строке, так и во второй
a, b = [set(input().split()) for _ in range(2)]
c = a & b

print(len(c))


# Все числа в порядке возрастания, которые есть как в первой строке, так и во второй
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = a & b

print(*sorted(c))


# Выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = a - b

print(*sorted(c))


# Все общие цифры в порядке возрастания у всех введенных чисел
n = int(input())

set_lst = [set(input()) for _ in range(n)]
set_str = set_lst[0]

for i in range(1, len(set_lst)):
    set_str.intersection_update(set_lst[i])

print(*sorted(set_str))