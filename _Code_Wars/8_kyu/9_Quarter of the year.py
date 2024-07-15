def quarter_of(month):

    return (month - 1) // 3 + 1
    return (month + 2) // 3
    return ceil(month / 3)


print(quarter_of(3, 1))
print(quarter_of(8, 3))
print(quarter_of(11, 4))


def quarter_of(month):
    year ={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}
    for k, v in year.items():
        if month in v:
            return k