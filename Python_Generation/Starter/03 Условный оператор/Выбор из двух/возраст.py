# Напишите программу, которая по введённому возрасту пользователя сообщает,
# к какой возрастной группе он относится

age = int(input())
if 0 <= age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')


age = int(input())
if age <= 13:
    print('детство')
elif age <= 24:
    print('молодость')
elif age <= 59:
    print('зрелость')
else:
    print('старость')
