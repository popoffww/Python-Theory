# Убить дракона двумя пулями; на каждого дракона - 2 пули
def hero(bullets, dragons):

    if bullets / dragons >= 2:
        if dragons == 0:
            print('Divided by zero')
        return True
    return False

print(hero(10, 5), True)
print(hero(7, 4), False)
print(hero(4, 5), False)
print(hero(100, 40), True)
print(hero(1500, 751), False)
print(hero(0, 1), False)


def hero(bullets, dragons):
    return bullets >= dragons * 2

def hero(bullets, dragons):
    return dragons <= bullets / 2