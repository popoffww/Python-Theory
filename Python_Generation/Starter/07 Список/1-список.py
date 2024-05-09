# Список чисел
number = int(input())
print(list(range(1, number + 1)))

# Список латинских букв
number = int(input())
string = ''
for i in range(number):
    string += chr(ord('a') + i)

print(list(string), end=' ')

# Добавление следующей буквы в список
array = []
for i in range(26):
    array.append(chr(ord('a') + i))
    print(array)

# Сумма минимального и максимального элементов списка
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(min(numbers) + max(numbers))

# Cреднее арифметическое элементов списка
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)

# Замена
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)

# Операторы конкатенации + и умножения списка на число *
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
numbers4 = ([1, 2, 3] * 2 + [6] * 9 + numbers3)
print(numbers4)

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers)) # длина списка
print(numbers[-1]) # последний элемент списка
print(numbers[::-1]) # список в обратном порядке
if (5, 17) in numbers: # список содержит числа 5 и 17
    print('YES')
else:
    print('NO')
print(numbers[1:-1]) # список с удаленными первым и последним элементами

