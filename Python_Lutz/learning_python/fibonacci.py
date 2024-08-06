import functools
from datetime import datetime


num = int(input())
a = 0
b = 1
while num:
    print(b, end=' ')
    a, b = b, a + b
    num -= 1



def fib():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second

f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

print('Быстрый вывод')



@functools.lru_cache(maxsize=None)
def fib(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 31):
     print(fib(i))

start = datetime.now()
print(datetime.now() - start)  # скорость вычисления


