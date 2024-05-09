# 01
print('*'*17)
print('*','*',sep='               ')
print('*','*',sep='               ')
print('*'*17)


# 02
# input(3 2)
a = int(input())
b = int(input())
sum = a + b
quadrat_1 = (a + b) * (a + b)
quadrat_2 = (a * a) + (b * b)
print('Квадрат суммы', a, 'и', b, 'равен', quadrat_1)
print('Сумма квадратов', a, 'и', b, 'равна', quadrat_2)


a = int(input())
b = int(input())
sum = int(a * a) + int(b * b)
quadrat = int(a + b) * int(a + b)
print('Квадрат суммы', a, 'и', b, 'равен', quadrat)
print('Сумма квадратов', a, 'и', b, 'равна', sum)


# 03
# input(9 29 7 27)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(a) ** int(b)
f = int(c) ** int(d)
print(e + f)


# 04
# input(1)
n = int(input())
f = str(n)
b = f + f
c = f + f + f
x = int(b) + int(c) + n
print(x)


number = int(input())
str_1 = str(number)
str_2 = str_1 + str_1
str_3 = str_1 + str_1 + str_1
int_1 = int(str_2)
int_2 = int(str_3)
summary = number + int_1 + int_2
print(summary)

# ==========================
# input(1)
n=int(input('Число от 1 до 9: \n'))
string=(f'{str(n)} + {str(n)*2} + {str(n)*3}')
print (f'{string} = {eval(string)}')