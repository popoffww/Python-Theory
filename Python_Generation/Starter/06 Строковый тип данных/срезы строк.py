# На вход программе подается строка текста.
# Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран

# Мое решение - громоздкое
string = input()
string_1 = string[: len(string) // 2]
string_2 = string[len(string) // 2 :]

if len(string) % 2 == 0:
    string_1 = string_1
    string_2 = string_2
else:
    string_1 = string[: len(string) // 2 + 1]
    string_2 = string_2[1:]

string_3 = string_2 + string_1
print(string_3)

# Изящное решение
string = input()
# length = len(string)

string_1 = string[:(len(string) + 1) // 2]
string_2 = string[(len(string) + 1) // 2:]

print(string_2 + string_1)

# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними
string = input()

before = string[:string.find('h')]
after = string[string.rfind('h') + 1:]

print(before, after, sep='')


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


# Напишите программу, которая определяет, является строка палиндромом
string = input()

if string == string[::-1]:
    print('YES')
else:
    print('NO')

# Второй вариант
string = input()
palindromes = [c for c in string if string == string[::-1]]
if palindromes:
    print('Да, это - палиндром')
else:
    print('Нет, это - не палиндром')


# Числовой палиндром - списочное выражение
palindromes = [i for i in range(1, 100) if str(i) == str(i)[::-1]]
print(*palindromes, len(palindromes), sep='\n')



# Срезы
string = input()

# исходная строка, повторенная 3 раза
print(string * 3)

# общее количество символов в строке
print(len(string))

# все символы в обратном порядке
print(string[::-1])

# все символы с четными индексами
print(string[::2])

# все символы с нечетными индексами
print(string[1::2])

# все символы строки через один в обратном порядке, начиная с последнего
print(string[-1::-2])

# строка с удаленным первым и последним символами
print(string[1:-1])

# вся строка, кроме последних двух символов
print(string[:-2])

# последние три символа строки
print(string[-3:])

# предпоследний символ строки
print(string[-2:-1])

# первый символ строки
print(string[0])

# первые три символа строки
print(string[:3])

# первые пять символов строки
print(string[:5])

# третий символ этой строки
print(string[2:3])








