# 97-122 - маленькие латинские буквы
# 65-90 - большие латинские буквы
# 1040-1071 - большие кириллица, 1025 - Ё
# 1072-1103 - большие кириллица, 1105 - ё
n = int(input())

letters = ''
for i in range(n):
    letters += chr(ord('a') + i)

print(list(letters))


letts = ''
for i in range(n):
    letts += chr(1040 + i)

print(list(letts))