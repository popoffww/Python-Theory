def sum_mix(arr):

    total = [int(i) for i in arr]

    return sum(total)

print(sum_mix([9, 3, '7', '3']), 22)
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']), 41)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)


def sum_array(a):

    num = [i for i in a]
    return sum(num)

print(sum_array([]), 0)
print(sum_array([1, 2, 3]), 6)
print(sum_array([1, 5.2, 4, 0, -1]), 9.2)