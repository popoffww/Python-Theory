import sys

'''as_integer_ratio, который удобно использовать для
преобразования вещественного числа в рациональное, 
а также метод is_integer
method, который проверяет – можно ли представить вещественное число 
как целое значение

X = 99
bin(X), X.bit_length()
(‘0b1100011’, 7)
bin(256), (256).bit_length()
(‘0b100000000’, 9)
len(bin(256)) - 2
9
'''

# функция getrefcount из стандартного модуля sys возвращает значе-
# ние поля счетчика ссылок в объекте
a=[1]
b=[1]
print(a is b,a.__eq__(b)) #False

a=1
b=1
print(a is b,a.__ne__(b)) #True малые целые числа и строки кэшируются и используются повторно

print(sys.getrefcount(1))

a = 'spam'
b = a
b = 'spam'
print(a, b, a.__eq__(b), a is b)

a = ['spam']
b = a
b[0] = 'shrubbery'
print(a, b, a.__eq__(b), a is b)

a = ['spam']
b = a[::]
b[0] = 'shrubbery'
print(a, b, a.__ne__(b), a is b)

