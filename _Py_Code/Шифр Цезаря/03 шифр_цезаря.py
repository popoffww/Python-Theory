# Сдвиг шифра
n = int(input())
s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for c in s:
    # ищем индекс текущей буквы в строке алфавита
    ind = alphabet.index(c)
    # находим новую букву
    new_c = alphabet[ind - n]

    print(new_c, end='')



n = int(input())
s = input()

for c in s:
    if ord(c) - n < 97:
        print(chr(ord(c) - n + 26), end='')
    else:
        print(chr(ord(c) - n), end='')