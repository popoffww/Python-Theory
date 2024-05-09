# Слова в столбик
string = input()
words = string.split()
array = list(words)
print(*array, sep='\n')
# или
string = input().split()
print(*string, sep='\n')

# Ф.И.О.
string = input().split()
name = string[0]
surname = string[1]
surname_2 = string[2]
print(name[0], surname[0], surname_2[0], sep='.', end='.')

# Убрать обратный слэш \
string = input().split('\\')
print(*string, sep='\n')
# или
print(input().replace('\\', '\n'))

# Линейчатая диаграмма (барчарт) из плюсиков
string = input().split()
number = 0
for c in string:
    # если += - неправильно
    number = + int(c)
    print('+' * number)
# или
string = input().split()
for c in string:
    print('+' * int(c))

# Корректный ip-адрес
string = input().split('.')
if 0 <= int(string[0]) <= 255 and \
        0 <= int(string[1]) <= 255 and \
        0 <= int(string[2]) <= 255 and \
        0 <= int(string[3]) <= 255:
    print('ДА')
else:
    print('НЕТ')

# Второй вариант
string = input().split('.')
for c in string:
    if not (0 <= int(c) <= 255):
        print('НЕТ')
        break
else:
    print('ДА')


# Добавь разделитель
string = input()
sign = input()
string_2 = sign.join(string)

print(string_2)


# Количество совпадающих пар
string = input().split()
array = list(string)
counter = 0

# цикл проходит от первого индекса: 0
for i in range(0, len(array) - 1):
# цикл проходит от второго индекса: 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            counter += 1
print(counter)