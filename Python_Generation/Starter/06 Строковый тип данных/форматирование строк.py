# (Не) Активное похудение
day = int(input())
weight = float(input())
target = 100 - day * 0.2

if weight <= target :
    print("Все идет по плану")
    print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {round(target, 1)} кг")
else:
    print("Что-то пошло не так")
    print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {(weight)} кг, ЦЕЛЬ по ВЕСУ = {round(target, 1)} кг")


# Мой ответ
day = int(input())
weight = float(input())
target = 100
flag = False

for i in range(1, 61):
    target -= 0.2
    # 16 день: 96.8000 не засчитывается
    # Надо ввести округление
    target = round(target, 1)
    if weight <= target:
        flag = True
    elif weight > target:
        flag = False

    if i == day and flag == True:
        print("Все идет по плану")
        print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {round(target, 1)} кг")
    elif i == day and flag == False:
        print("Что-то пошло не так")
        print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {round(target, 1)} кг")

# Вывод веса по дням
day = int(input())
target = 100

for i in range(1, 61):
    target -= 0.2
    # print(i, round(target, 1))
    if i == day:
        print(i, round(target, 1))