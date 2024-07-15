# Преобразование строки в дату-время
from datetime import date, time
from datetime import datetime

day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')

my_date = date(int(year), int(month), int(day))        # создаем объект типа date
my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time

print(my_date)
print(my_time)



datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')

date_str, time_str = datetime_str.split(' ')

date_info = [int(i) for i in date_str.split('.')]
time_info = [int(i) for i in time_str.split(':')]

my_datetime = datetime(date_info[2], date_info[1], date_info[0], time_info[0], time_info[1], time_info[2])

print(my_datetime)


