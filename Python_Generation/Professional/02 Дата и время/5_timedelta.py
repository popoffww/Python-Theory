from datetime import date, datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
print(dt.strftime('%d.%m.%Y %H:%M:%S'))


today = date(2021, 11, 4)
birthday = date(2022, 10, 6)
days = (birthday - today).days
print(days)


# Предыдущая и следующая даты
today = datetime.strptime(input(), '%d.%m.%Y')

print((today - timedelta(days=1)).strftime('%d.%m.%Y'))
print((today + timedelta(hours=24)).strftime('%d.%m.%Y'))


# Количество секунд
hour, min, sec = map(int, input().split(':'))
td = timedelta(hours=hour, minutes=min, seconds=sec)

print(int(td.total_seconds()))


# Какое время будет на часах, когда прозвенит таймер
