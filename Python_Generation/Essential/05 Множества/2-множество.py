# Количество уникальных символов для каждого слова без учета регистра
number = int(input())
for i in range(number):
    string = input().lower()
    set_str = set(string)

    print(len(set_str))


# Количество уникальных символов во всех считанных словах без учета регистра
number = int(input())
array = []
for _ in range(number):
    string = input().lower()
    array.extend(string)
    set_str = set(array)

print(len(set_str))

# Оптимальное решение
n = int(input())
symbols = set()
for _ in range(n):
    for c in input().lower():
        symbols.add(c)

print(len(symbols))


# Общее количество различных слов в строке текста
string = input().lower()
symbols_to_remove = ".,;:-?!"
for symbol in symbols_to_remove:
    string = string.replace(symbol, "")

set_str = set(string.split())
print((len(set_str)))

# Оптимальное решение
words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(len(set(words)))


# Встречалось ли число раньше?
array = [int(i) for i in input().split()]
set_str = set()

for c in range(len(array)):
    if array[c] in set_str:
        print('YES')
    else:
        print('NO')
        set_str.add(array[c])