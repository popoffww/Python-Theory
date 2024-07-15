from datetime import date

my_date = date(1973, 4, 11)
my_num_date = my_date.toordinal()
begin = date.fromordinal(1)

print(f'Я родился {my_date.day}.0{my_date.month}.{my_date.year}, в {my_date.isoweekday()} день недели.')
print(f'Это был {my_num_date} день, начиная с даты {begin}.')


# Квартал
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

quartal = ''
for i in dates:
    if i.month in (1, 2, 3):
        quartal = 'Q1'
    if i.month in (4, 5, 6):
        quartal = 'Q2'
    if i.month in (7, 8, 9):
        quartal = 'Q3'
    if i.month in (10, 11, 12):
        quartal = 'Q4'

    print(f'{i.year}-{quartal}')

# или
quarters = {'Q1': [1, 2, 3], 'Q2': [4, 5, 6], 'Q3': [7, 8, 9], 'Q4': [10, 11, 12]}
for date in dates:
    for q in quarters:
        if date.month in quarters[q]:
            print(date.year,q, sep = '-')
# или
for d in dates:
    print(f'{d.year}-Q{(d.month - 1) // 3 + 1}')


# Минимум-максимум
def get_min_max(dates):
    if dates:
        return min(dates), max(dates)
    return ()

dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))


# Диапазон дат
def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')


# Количество суббот
def saturdays_between_two_dates(start, end):

    if start > end:
        start, end = end, start

    return sum([date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1)])

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
