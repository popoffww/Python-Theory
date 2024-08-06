# Сумма соседних чисел
_range = int(input())
array = []
value = 0

for i in range(_range):
    number = int(input())

    value += number
    array.append(value)
    value = number

print(array[1:])


# Самый частотный символ
string = input()

counter = 0
result = ''

for c in string:
    symbol = string.count(c)
    if symbol >= counter:
        counter = symbol
        result = c

print(result)

# Через длину строки
counter = 0
result = ''

for i in range(len(string)):
    symbol = string.count(string[i])
    if symbol >= counter:
        counter = symbol
        result = string[i]

print(result)