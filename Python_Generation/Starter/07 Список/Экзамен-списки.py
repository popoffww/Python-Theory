# Список четных
numbers = int(input())

array = [i for i in range(2, numbers + 1) if i % 2 == 0]
print(array)


# Сумма двух списков
string_1 = input().split()
string_2 = input().split()

total = [int(string_1[i]) + int(string_2[i]) for i in range(len(string_1))]
print(*total)


# Сумма чисел
numbers = input().split()

counter = 0
for i in numbers:
    counter += int(i)
    ciffres = '+'.join(numbers)

print(ciffres, counter, sep='=')


# Валидный номер
number = [i for i in input().split('-')]

string = [len(j) for j in number]

if ''.join(number).isdigit() and string == [3, 3, 4]:
    print('YES')
elif ''.join(number).isdigit() and string == [1, 3, 3, 4] and number[0] == '7':
    print('YES')
else:
    print('NO')


# Самый длинный
string = input().split()

array = [len(c) for c in string]
print(max(array))


# Молодежный жаргон
string = input().split()

array = [c[1:] + c[0] + 'ки' for c in string]
print(*array)