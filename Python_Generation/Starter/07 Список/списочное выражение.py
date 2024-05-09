# Получить новый список, содержащий строки исходного списка,
# где у каждой строки удалён первый символ
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1:] for m in keywords]
print(new_keywords)

# Получить новый список, содержащий длины строк исходного списка
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

# Получить новый список, содержащий только слова длиной не менее пяти символов (включительно)
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m for m in keywords if len(m) >= 5]
print(new_keywords)

# Получить список всех чисел-палиндромов от 100100 до 10001000 (включительно)
palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindromes)

string = input()
palindromes = [c for c in string if string == string[::-1]]
if palindromes:
    print('Да, это - палиндром')
else:
    print('Нет, это - не палиндром')


# Списочное выражение, которая создает список, содержащий квадраты чисел от 1 до n(включительно)
_range = int(input())
array = [i ** 2 for i in range(1, _range + 1)]
print(*array, sep='\n')


# Списочное выражение, которая выведет кубы указанных чисел также на одной строке
string = input().split()
array = [int(string[i]) ** 3 for i in range(len(string))]
print(*array)


# Списочное выражение выводит слова введенной строки в столбик
string = input().split()
array = [c for c in string]
print(*array, sep='\n')


# Списочное выражение выводит все цифровые символы данной строки
string = input()
array = [c for c in string if c.isdigit()]
print(*array, sep='')


# Сисочное выражение выводит не оканчивающиеся на цифру 44 квадраты четных чисел
string = input().split()
array = [int(c) ** 2 for c in string if int(c) % 2 == 0 and int(c) ** 2 != 4 and int(c) ** 2 % 10 != 4]
print(*array)