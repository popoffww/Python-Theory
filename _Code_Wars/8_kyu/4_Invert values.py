import operator

def invert(lst):

    return list(map(operator.neg, lst))
    return [-x for x in lst]
    return [x * -1 for x in lst]

print(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
print(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])


def invert(lst):
    result = list()
    for num in lst:
        result.append(-num)
    return result