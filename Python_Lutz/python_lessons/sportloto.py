import random

print("Результат тиража 'Спортлото 6 из 36'")
sport_loto = list(range(1, 37))
win_num = 0
while win_num <= 5:
    win_num += 1
    win_loto = (random.choice(sport_loto))
    print('\tВыиграло {}-ое число: '.format(win_num), win_loto)

print("Результат тиража 'Спортлото 5 из 35'")
sport_loto = list(range(1, 36))
win_num = 0
while win_num <= 4:
    win_num += 1
    win_loto = (random.choice(sport_loto))
    print('\tВыиграло {}-ое число: '.format(win_num), win_loto)



# l = list(range(6))
# n1 = (random.choice(l))
# a = 0
# while a <= 3:
#     a += 1
#     n2 = int(input('Enter number 0 - {}: '.format(len(l))))
#     if n2 != n1:
#         print('You\'re lost')
#         continue
#     else:
#         print('You\'re win')
#         break