import random

a = []
b = []

for _ in range(10):
    x = random.randint(1, 51)
    y = random.randint(1, 51)

    a.append(x)
    b.append(y)

c = set(a)
d = set(b)
cs = sorted(c)
ds = sorted(d)

print('Множество №1:', cs, sep='\n')
print('Множество №2:', ds, sep='\n')
print('=' * 30)

e = c & d
es = sorted(e)
f1 = c - d
f2 = d - c
f1s = sorted(f1)
f2s = sorted(f2)
g = c ^ d
gs = sorted(g)
print('Совпадения:', es, sep='\n')
print('Всего:', len(es))
print('=' * 30)
print('Разница №1-№2:', f1s, sep='\n')
print('Всего:', len(f1s))
print('*' * 10)
print('Разница №2-№1:', f2s, sep='\n')
print('Всего:', len(f2s))
print('=' * 30)
print('Симметрическая разность:', gs, sep='\n')
print('Всего:', len(gs))