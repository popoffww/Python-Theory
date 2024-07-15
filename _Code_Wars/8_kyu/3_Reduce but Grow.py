from functools import reduce
import operator, math

def grow(arr):

   mult = reduce(operator.mul, arr)
   return mult


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


def grow(arr):
    return math.prod(arr)


def grow(arr):

    mult = 1
    for i in arr:
        mult *= i

        return mult

print(grow([6, [1, 2, 3]]))
print(grow([16, [4, 1, 1, 1, 4]]))
print(grow([64, [2, 2, 2, 2, 2, 2]]))