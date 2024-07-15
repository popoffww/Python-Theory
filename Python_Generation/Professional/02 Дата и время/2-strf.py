from datetime import date, time

alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))


birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))


andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# Минимальная дата из двух
date_1 = date.fromisoformat(input())
date_2 = date.fromisoformat(input())

minimum = min(date_1, date_2)
print(minimum.strftime('%d-%m (%Y)'))


# Сортировка дат
input_date = [date.fromisoformat(input()) for _ in range(int(input()))]
for d in sorted(input_date):
    print(d.strftime('%d/%m/%Y'))


# 29 = 1992
def print_good_dates(dates):
    for i in sorted(filter(lambda d: d.month + d.day == 29 and d.year == 1992, dates)):
        print(i.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)


# Корректная дата
from datetime import date

def is_correct(day, month, year):
    try:
       correct_date = date(year, month, day)
       return True
    except:
        return False

print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))


# 19.05.2016
# 05.13.2010
# 21.12.2012
# 01.01.1000
# 32.04.2003
def is_correct(day, month, year):
    try:
       correct_date = date(year, month, day)
       return True
    except:
        return False

count = 0
input_date = input()
while input_date != 'end':
    day, month, year = input_date.split('.')
    # if is_correct(*map(int, input_date.split('.'))):
    if is_correct(int(day), int(month), int(year)):
        count += 1
        print('Корректная')
    else:
        print('Некорректная')

    input_date = input()

print(count)