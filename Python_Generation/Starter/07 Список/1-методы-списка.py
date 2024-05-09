numbers = [8, 9, 10, 11]
# замена второго элемента списка на 17
numbers[1] = 17
# 4, 5, 6 в конец списк
numbers.append(4)
numbers.append(5)
numbers.append(6)
# удалить первый элемент списка
numbers.remove(8)
# удвоить список
numbers *= 2
# вставить число 25 по индексу 3
numbers.insert(3, 25)
print(numbers)


# Количество артиклей
string = input().split()
a = string.count('a')
A = string.count('A')
an = string.count('an')
An = string.count('An')
the = string.count('the')
The = string.count('The')
total = (a + A + an + An + the + The)
print('Общее количество артиклей:',total)
# или
string = input().lower().split()
a = string.count('a')
an = string.count('an')
the = string.count('the')
total = (a + an + the)
print('Общее количество артиклей:',total)


# Сортировка чисел
# Цикл обязательно
string = input().split() # без split() - ошибка
array = []
array_2 = []
for c in string:
    array.append(int(c))
    array_2.append(int(c))
    array.sort()
    array_2.sort(reverse=True)
print(*array)   # print(array.sort()) - None
print(*array_2) # print(array.sort(reverse=True)) - None


# Удалить комментарий кода
string = int(input()[1:])
array = []
for i in range(string):
    # text = input() = print("Здравствуйте, старейшина", name)  # Элайджа вперёд
    text = input()
    if '#' in text:
        text = text[:text.find('#')]
        text = text.rstrip()
    array.append(text)

print(*array, sep='\n')


# Переставить min и max
string = input().split()
array = []

for c in string:
    array.append(int(c))

maximum = max(array)
minimum = min(array)
max_index = array.index(maximum)
min_index = array.index(minimum)

array[max_index], array[min_index] = array[min_index], array[max_index]
print(*array)