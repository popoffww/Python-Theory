for i in range(10):
    string = 'Python is awesome!'
    print(string)

string = input()
number = int(input())
for i in range(number):
    print(string)


number = int(input())
for i in range(number):
    print('*' * 19)


number = int(input())
for i in range(number, 0, -1):
    print('*' * i)



for i in range(6):
    print('A' * 3)
for i in range(5):
    print('B' * 4)
print('E')
for i in range(9):
    print('T' * 5)
print('G')


string = input()
for i in range(10):
    print(i, string)



number = int(input())
for i in range(number + 1):
    print('Квадрат числа', i, 'равен', i * i)



# Напишите программу, которая предсказывает размер популяции организмов
# с 1-го по n-й день(включительно). Программа должна выводить номер дня,
# а затем через пробел размер популяции в этот день

# стартовое количество организмов
m = int(input())
# среднесуточное увеличение в %
p = int(input())
# количество дней для размножения
n = int(input())

for i in range(0, n):
    units = m * (1 + p / 100) ** i
    print(i+1, units)