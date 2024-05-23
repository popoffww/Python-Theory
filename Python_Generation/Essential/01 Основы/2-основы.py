# Координатные четверти
first = 0
second = 0
third = 0
fourth = 0

for _ in range(int(input())):
    coordinate = input().split()
    if int(coordinate[0]) > 0:
        if int(coordinate[1]) > 0:
            first += 1
        elif int(coordinate[1]) < 0:
            fourth += 1
    if int(coordinate[0]) < 0:
        if int(coordinate[1]) > 0:
            second += 1
        elif int(coordinate[1]) < 0:
            third += 1

print('Первая четверть:', first)
print('Вторая четверть:', second)
print('Третья четверть:', third)
print('Четвертая четверть:', fourth)


# Подсчет количества чисел, которые больше предшествующего в этом списке
array = [int(i) for i in input().split()]
counter = 0

for j in range(1, len(array)):
    if array[j] > array[j - 1]:
        counter += 1
print(counter)


# Замена соседних элементов списка
array = [int(i) for i in input().split()]

for j in range(0, len(array) - 1, 2):
    array[j], array[j + 1] = array[j + 1], array[j]

print(*array)



# Последний элемент становится первым, а остальные сдвигаются
# на одну позицию вперед, в сторону увеличения индексов
string = input().split()

array = [c for c in string]
print(array[-1], *array[:-1])
# или
print(string[-1] + string[:len(string) - 1])


# Подсчет количества разных элементов в списке
array = input().split()
array_2 = []

for li in array:
    if li not in array_2:
        array_2.append(li)

print(len(array_2))


# Является ли число произведением двух чисел из данного набора
number = [int(input()) for _ in range(int(input()))]
multi = int(input())

flag = False

for i in range(len(number)):
    for j in range(len(number)):
        if number[i] * number[j] == multi and i != j:
            flag = True
            break
if flag:
    print('ДА')
else:
    print('НЕТ')



# Камень, ножницы, бумага
timur = input()
ruslan = input()

won = ''

if timur == 'камень' and ruslan == 'бумага' or timur == 'бумага' and ruslan == 'камень':
    won += 'бумага'
    if won == timur:
        print('Тимур')
    else:
        print('Руслан')

elif timur == 'камень' and ruslan == 'ножницы' or timur == 'ножницы' and ruslan == 'камень':
    won += 'камень'
    if won == timur:
        print('Тимур')
    else:
        print('Руслан')

elif timur == 'ножницы' and ruslan == 'бумага' or timur == 'бумага' and ruslan == 'ножницы':
    won += 'ножницы'
    if won == timur:
        print('Тимур')
    else:
        print('Руслан')

elif timur == ruslan:
    print('ничья')

# Расположили список возможных ходов в таком порядке,
# что каждая текущая фигура бьет следующую.
# Соответственно при вычитании индексов в случае победы или поражение будет точно не 0.
# Значит для списка результатов надо смотреть уже кого ставить первым
# в зависимости от очередности ходов.
# Тимур ходит ножницами, а Руслан бумагой, разница в индексах -1, что эквивалентно индексу 2.
# Значит мы понимаем, что в таком случае победа Тимура должна быть на 2 индексе

options = ["камень", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]
print(res)


# Камень, ножницы, бумага, ящерица, Спок
# Расположили список возможных ходов так, что для любых двух соседей первый бьёт второго
options = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур",]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]
print(res)


# Предикат делимости
def func(num1, num2):

    if num1 % num2 == 0:
        return True
    return False

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('делится')
else:
    print('не делится')


# Тип данных bool 3.1. Предикат делимости
def func(num1, num2):

    if num1 % num2 == 0:
        return True
    return False

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('делится')
else:
    print('не делится')


# Кремниевая долина
# Если в строке присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
virus = 'anton'

for i in range(1, int(input()) + 1):
    string = input()
    result = ''
    for c in virus:
        if c in string:
            result += c
            string = string[string.find(c):]
    if result == virus:
        print(i, end=' ')


# Роскомнадзор запретил букву а
word = input() + ' запретил букву'

a = ord('а')
for i in range(a, a + 32):
    if chr(i) in word:
        print((word.strip() + ' ' + chr(i)))
        word = (word.replace(chr(i), ''))
        word = word.replace('  ', ' ')

print('=' * 20)

word = input() + ' запретил букву'

alphabet = [chr(i) for i in range(1072, 1104) if chr(i) != 'ё']
for c in alphabet:
    if c in word:
        print(word, c)
        word = word.replace(c, '').replace(' ', ' ').strip()