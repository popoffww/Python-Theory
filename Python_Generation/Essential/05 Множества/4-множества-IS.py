# Одинаковые цифры
a, b = [set(input()) for _ in range(2)]

if a.isdisjoint(b):
    print('NO')
else:
    print('YES')

# Изящное решение
s1 = set(input())
s2 = set(input())

have_common_digits = not s1.isdisjoint(s2)
print(("NO", "YES")[have_common_digits])


# Входят ли в запись первого числа все цифры, содержащиеся в записи второго
a1, b1 = [(input()) for _ in range(2)]

a = []
b = []
a.extend(a1)
b.extend(b1)

c = set(a)
d = set(b)

if c.issuperset(d):
    print('YES')
else:
    print('NO')

# или
set1, set2 = set(input()), set(input())

print(("NO", "YES")[set1 >= set2])


# Множество элементов, которые есть и у первого, и у второго, но нет у третьего множества
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = set((int(i)) for i in input().split())

d = a & b
e = d - c
print(*sorted(e, reverse=True))
# или
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set1 & set2 - set3, reverse=True))


# Оценки, которые встречаются не более, чем у двух учеников
# Или по-другому
# Все возможные оценки трех учеников минус оценки, которые встречаются одновременно у всех трех
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = set((int(i)) for i in input().split())

d = a | b | c
e = a & b & c
f = d - e
print(*sorted(f))
# или
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))


# Множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = set((int(i)) for i in input().split())

d = a | b
e = c - d
print(*sorted(e, reverse=True))
# или
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set3 - set2 - set1, reverse=True))


# Множество оценок, не встречающихся ни у одного из трех учеников
a = set((int(i)) for i in input().split())
b = set((int(i)) for i in input().split())
c = set((int(i)) for i in input().split())
d = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

e = a | b | c
f = d - e

print(*sorted(f))
# или
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set(range(11)) - set1 - set2 - set3))