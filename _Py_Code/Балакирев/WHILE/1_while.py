# osnovnye--metody-----slovarey
s = input()

count = len(s)
simbol = '--'

while count != 0:
    s = s.replace(simbol,'-')
    count -= 1

print(s)


# или
while '--' in s:
    s = s.replace('--', '-')
print(s)


# Фибоначчи
num = int(input())

a = 0
b = 1

while num:
    print(b, end=' ')
    a, b = b, a + b
    num -= 1



# Амебы
n = int(input())  # Пользовательский ввод

amebs = 1  # Счетчик амеб
clocs_div = n / 3  # Сколько раз за все время амебы поделились
count = 1  # Счетчик

while count < clocs_div:
    amebs = amebs * 2  # Сколько получилось амеб
    count += 1  # Увеличиваю счетчик на 1

print(round(amebs))  # Округляю полученный результат и вывожу в консоль


# Гражданин 1 января открыл счет в банке, вложив 1000 руб.
# Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
# Определить сумму вклада через n лет
n = int(input())

amount = 1000
while n > 0:
    amount += amount * 0.05
    n -= 1

print(round(amount, 2))
# или
amount = 1000
year = 0
while n != year:
    amount += amount * 0.05
    year += 1
print(round(amount, 2))



# Нечетные числа
n, m = map(int, input().split())

while n <= m:
    if n % 2 == 1:
        print(n, end=' ')
    n += 1



# Все трехзначные числа, которые при делении на 47 дают в остатке 44 и кратны 3
n = 100

while 100 <= n <= 999:
    if n % 47 == 44 and n % 3 == 0:
        print(n, end=' ')
    n += 1