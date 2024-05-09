

print(""" Выберите номер операции:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
    """)
operation = input('Введите номер операции: ')
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
result = int()
if operation == '1':
    result = number1 + number2
elif operation == '2':
    result = number1 - number2
elif operation == '3':
    result = number1 * number2
elif operation == '4':
    result == number1 / number2
else:
    result = number1 % number2
print('Результат: {}'.format(result))

