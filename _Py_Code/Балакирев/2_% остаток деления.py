# Работа светофора для пешеходов запрограммирована следующим образом:
# в начале каждого часа в течение трех минут горит зеленый сигнал,
# затем в течение двух минут – красный, в течение трех минут – опять зеленый и т. д.,
# процесс повторяется.
n = float(input())

if n % 5 <= 3:
    print('green')
else:
    print('red')


# Дни недели
k = int(input())

week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

if k % 7 == 1:
    print(week[0])
elif k % 7 == 2:
    print(week[1])
elif k % 7 == 3:
    print(week[2])
elif k % 7 == 4:
    print(week[3])
elif k % 7 == 5:
    print(week[4])
elif k % 7 == 6:
    print(week[5])
elif k % 7 == 7:
    print(week[6])