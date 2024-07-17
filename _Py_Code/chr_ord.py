import string
# 65-90 - большие латинские буквы
# 97-122 - маленькие латинские буквы
# 1040-1071 - большие кириллица, 1025 - Ё
# 1072-1103 - маленькие кириллица, 1105 - ё
n = int(input())

letters = ''
for i in range(n):
    letters += chr(ord('a') + i)

print(list(letters))


letts = ''
for i in range(n):
    letts += chr(1040 + i)

print(list(letts))



letters = ''
for i in range(26):
    letters += chr(97 + i)
print(letters)



print(*[chr(el) for el in range(97, 123)], sep='\n')



for i in range(97,123):
    print(chr(i))


letters = [i for i in enumerate(string.ascii_lowercase, 1)]
dct = {el[1]: el[0] for el in letters}
print(dct)