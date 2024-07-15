import random
# Содержимое файла
file = open(input(), encoding='utf-8')

print(file.read())
file.close()

# Предпоследняя строка
file = open(input(), encoding='utf-8')

print(file.readlines()[-2])
file.close()

# Случайная строка
file = open(input(), encoding='utf-8')
content = file.readlines()
print(random.choice(content))
# или
content = set(file.readlines()).pop()
print(content)

file.close()

# Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число
# Напишите программу, выводящую на экран сумму этих чисел
file = open('numbers.txt', encoding='utf-8')
content = sum(map(int, file))
print(content)

file.close()


# В файле nums.txt записано два целых числа, они могут быть разделены символами пробела и конца строки
# Напишите программу, выводящую на экран сумму этих чисел
file = open('nums.txt', encoding='utf-8')
content = sum(map(int, file.read().split()))
print(content)

file.close()


# Общая стоимость
file = open('prices.txt', encoding='utf-8')
total = 0

for el in file:
    good = el.split()
    total += int(good[1]) * int(good[2])

print(total)

file.close()