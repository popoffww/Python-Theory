from functools import reduce

def func(x, y):
    return x + y

nums = list(range(1, 11))
# Вызов фукции
total = reduce(func, nums, 0)
# или такой вызов
total = reduce(func, nums)
print(nums)
print('Сумма:', total, end='.')