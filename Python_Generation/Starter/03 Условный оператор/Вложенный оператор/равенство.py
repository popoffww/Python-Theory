# Даны три целых числа.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или
# 0 (если все числа различны).
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)


a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)

a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)