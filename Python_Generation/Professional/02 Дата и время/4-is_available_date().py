from datetime import datetime, date

def is_available_date(dates, some_date):
    def get_number(x):

        start = date.toordinal(datetime.strptime((x.split('-')[0]), '%d.%m.%Y'))
        stop = date.toordinal(datetime.strptime((x.split('-')[-1]), '%d.%m.%Y'))
        return list(range(start, stop + 1))


    set_a = set()
    set_b = set(get_number(some_date))

    for i in dates:
        for j in get_number(i):
            set_a.add(j)

    if set_a.intersection(set_b):
        return False
    return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))