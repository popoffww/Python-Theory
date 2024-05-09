# Конвертер километров
def convert_to_miles(km):

    miles = km * 0.6214
    return miles

num = int(input())
print(convert_to_miles(num))

# Количество дней
def get_days(month):

    if num == 2:
        return 28
    # elif num == 4 or num == 6 or num == 9 or num == 11:
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

num = int(input())
print(get_days(num))


# Делители
def get_factors(num):

    array = []
    counter = 0
    total = 0
    for i in range(1, n + 1):
        if num % i == 0:
            counter += i
            array.append(i)
            total += 1
    print(f"Всего делителей: {total}")
    return array

n = int(input())
print(f"Делители числа {n}:", get_factors(n), sep='\n')


# Список, содержащий все местоположения символа в строке
def find_all(target, symbol):

    return [i for i in range(len(target)) if target[i] == symbol]

s = input()
char = input()

print(find_all(s, char))


# Сортировка
def merge(list1, list2):

    array = list1 + list2
    array.sort()

    return array

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))


# Сортировка 2
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result

list1 = []

for _ in range(int(input())):
    list2 = [int(i) for i in input().split()]
    result = quick_merge(list1, list2)
    list1 = result

print(*result)