number = int(input())
num_1 = number % 10
num_2 = (number // 10) % 10
num_3 = number // 100
sum = num_1 + num_2 + num_3
multi = num_1 * num_2 * num_3
print(f'Сумма цифр = {sum}')
print(f'Произведение цифр = {multi}')


number = int(input())
d1 = (number // 10 ** 2) % 10
d2 = (number // 10 ** 1) % 10
d3 = (number // 10 ** 0) % 10
digits_sum = d1 + d2 + d3
digits_prod = d1 * d2 * d3
print("Сумма цифр = ", digits_sum, "\nПроизведение цифр = ", digits_prod, sep="")


number = int(input())
num_3 = number % 10
num_2 = (number // 10) % 10
num_1 = number // 100
print(f'{num_1}{num_2}{num_3}')
print(f'{num_1}{num_3}{num_2}')
print(f'{num_2}{num_1}{num_3}')
print(f'{num_2}{num_3}{num_1}')
print(f'{num_3}{num_1}{num_2}')
print(f'{num_3}{num_2}{num_1}')


number = int(input())
num_1 = number % 10
num_10 = (number // 10) % 10
num_100 = (number // 100) % 10
num_1000 = (number // 1000) % 10

print('Цифра в позиции тысяч равна',num_1000)
print('Цифра в позиции сотен равна',num_100)
print('Цифра в позиции десятков равна',num_10)
print('Цифра в позиции единиц равна',num_1)


a, b, c, d = input(), input(), input(), input()
print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')



number = int(input())
d1 = (number // 10 ** 2) % 10
d2 = (number // 10 ** 1) % 10
d3 = (number // 10 ** 0) % 10
print(d1, d2, d3, sep="")
print(d1, d3, d2, sep="")
print(d2, d1, d3, sep="")
print(d2, d3, d1, sep="")
print(d3, d1, d2, sep="")
print(d3, d2, d1, sep="")