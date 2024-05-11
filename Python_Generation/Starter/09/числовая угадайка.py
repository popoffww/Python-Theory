# Наименьшее количество попыток, которых гарантированно хватит, чтобы угадать число
from math import log, ceil

number = int(input())
attempt = ceil(log(number, 2))
print(attempt)