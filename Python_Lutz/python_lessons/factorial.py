
# factorial = int(1)
# number = int(4)
# while number > 0:
#     factorial = factorial * number
#     number -= 1
# print('Факториал числа 4! равен: ', factorial)

try:
    factorial = 1
    number = int(input("Введите число: "))
    while number > 0:
        factorial = factorial * number
        number -= 1
    print('Факториал равен: ', factorial)
    print('Факториал: %d'%factorial)
except EOFError as e:
    print(end="")
