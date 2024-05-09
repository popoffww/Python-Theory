def main():
    while True:
        try:
            number1 = float(input('Введите первое число: '))
            number2 = float(input('Введите второе число: '))
            print('Результат: ', number1 / number2)
            break
        except ZeroDivisionError as error1:
            print('Ошибка деления на ноль:', error1)
            print('Введите корректное второе число.')
        except ValueError as error2:
            print('Введена строка вместо числа:', error2)
            print('Попробуйте еще раз.')
    print(ZeroDivisionError.__mro__)


if __name__ == '__main__':
    main()


# try:
#     eval('#hfffdddh')
# except SyntaxError:
#     print('syntax error')





