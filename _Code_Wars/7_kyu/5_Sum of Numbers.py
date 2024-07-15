def get_sum(a, b):

    if a > b:
        a, b = b, a

    if a != b:
        return sum(range(a, b + 1))
    else:
        return a

    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(1, 100), 5050)
print(get_sum(54, -4958), -12291876)
print(get_sum(25678, -56852), -1286410697)