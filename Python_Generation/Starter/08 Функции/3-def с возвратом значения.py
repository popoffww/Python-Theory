# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами
# Простое решение в файле AND-OR-NOT.py
def is_valid_triangle(side1, side2, side3):

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))


# True если число является простым и False в противном случае
def is_prime(num):

    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

n = int(input())
print(is_prime(n))


# Сервое простое число, большее числа num
def get_next_prime(num):

    num += 1
    for i in range(2, num):
        # если число непростое
        if num % i == 0:
            # снова вызываем функцию, пока не найдется простое число
            return get_next_prime(num)
    # возвращаем простое число
    return num

n = int(input())
print(get_next_prime(n))

# Пароль является надежным если:
# его длина не менее 8 символов
# он содержит как минимум одну заглавную букву (верхний регистр)
# он содержит как минимум одну строчную букву (нижний регистр)
# он содержит хотя бы одну цифру
def is_password_good(password):
    if len(password) < 8 or \
            password.isupper() or \
            password.islower() or \
            password.isdigit() or \
            password.isalpha() or not password.isalnum():
        return False
    else:
        return True

txt = input()
print(is_password_good(txt))

# Второй способ
def is_password_good(password):
    if len(password) < 8:
        return False

    flag_1 = False
    flag_2 = False
    flag_3 = False

    for c in password:
        if c.isupper():
            flag_1 = True
        elif c.islower():
            flag_2 = True
        elif c.isdigit():
            flag_3 = True
    return flag_1 and flag_2 and flag_3

txt = input()
print(is_password_good(txt))


# Слова имеют одинаковую длину и отличаются ровно в одном символе
def is_one_away(word1, word2):

    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                counter += 1
        if counter + 1 == len(word1):
            return True
    return False

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))


# Палиндром
def is_palindrome(text):

    string = ''
    sign = ['.', ',', '!', '?', '-', ' ']
    for c in text:
        string += c
        string = string.lower()
        for s in sign:
            string = string.replace(s, '')

    return string == string[::-1]

txt = input()
print(is_palindrome(txt))

# Второй вариант - проще
def is_palindrome(text):

    sign = ['.', ',', '!', '?', '-', ' ']
    for с in sign:
        text = text.replace(с, '')

    text = text.lower()
    return text == text[::-1]

txt = input()
print(is_palindrome(txt))

# Пароль имеет вид a:b:c
# a – должно быть палиндромом
# b – должно быть простым
# c – должно быть четным
def is_valid_password(password):

    x = password.split(':')
    if len(x) != 3:
        return False

    a, b, c = x[0], x[1], x[2]
    flag1, flag2, flag3 = False, False, False

    if a == a[::-1]:
       flag1 = True

    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False
    flag2 = True

    if int(c) % 2 == 0:
        flag3 = True

    return flag1 and flag2 and flag3

psw = input()
print(is_valid_password(psw))


# Правильная скобочная последовательность
def is_correct_bracket(text):

    while '()' in text:
        text = text.replace('()', '')

    if text == '':
        return True

    return False

txt = input()
print(is_correct_bracket(txt))



# ВерблюжийРегистр в змеиный_регистр
def convert_to_python_case(text):

    for c in text:
        if c.isupper():
            text = text.replace(c, '_' + c.lower())
    text = text[1:]
    return text

txt = input()
print(convert_to_python_case(txt))
