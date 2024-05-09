# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы
string = input()
if string == string.title():
    print('YES')
else:
    print('NO')


# Замените все строчные символы заглавными и наоборот
string = input()
if string != string.swapcase():
    print(string.swapcase())


# Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах
string = input().lower()
if 'хорош' in string:
    print('YES')
else:
    print('NO')


# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре
string = input()
numbers = '1234567890'
count = 0

for c in string:
    if c == c.lower() and c not in numbers:
        count += 1

print(count)