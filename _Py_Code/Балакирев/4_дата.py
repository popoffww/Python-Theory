# Предыдущая и следующая дата
import datetime

# Считываем входящее число - k-й день невисокосного года, в формате разницы времени.
time_delta = datetime.timedelta(days=int(input())-1)

# Задаем текущую дату (2007 год - невисокосный, начинающийся с понедельника).
date_today = datetime.datetime(2007, 1, 1) + time_delta

# Создаем словарь наименований дня недели.
days_week = {0: 'воскресенье', 1: 'понедельник', 2: 'вторник',
             3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота'}
# Выводим результат - день недели k-го дня.

print(days_week[int(date_today.strftime('%w'))])