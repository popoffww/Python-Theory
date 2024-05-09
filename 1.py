def is_valid_password(password):

    x = password.split(':')
    if len(x) != 3:
        return False

    a, b, c = x[0], x[1], x[2]
    flag1, flag2, flag3 = False, False, False

    if a == a[::-1]:
       flag1 = True

    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False
    flag2 = True

    if int(c) % 2 == 0:
        flag3 = True

    return flag1 and flag2 and flag3

psw = input()
print(is_valid_password(psw))