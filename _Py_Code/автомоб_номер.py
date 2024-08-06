import string

# Верный номер: L - буква, N -цифра
# LNNNLL_NN или LNNNLL_NNN
s = input().upper()

res = ''

for c in s:
    # Латинский большой алфавит
    # if c in string.ascii_uppercase:
    if c.isalpha():
        res += 'L'
    # elif c in string.digits:
    elif c.isdigit():
        res += 'N'
    elif c == '_':
        res += '_'
    else:
        res += ' '

if res in ('LNNNLL_NN', 'LNNNLL_NNN'):
    print('Верный номер')
else:
    print('Неверный номер')


# Телефонный номер
s = input()

res = ''

for c in s[2:]:
    if c.isdigit():
        res += 'N'
    elif c == '+':
        res += '+'
    elif c == '(':
        res += '('
    elif c == ')':
        res += ')'
    elif c == '-':
        res += '-'

if res in ('+7(NNN)NNN-NN-NN'):
    print('ДА')
else:
    print('НЕТ')