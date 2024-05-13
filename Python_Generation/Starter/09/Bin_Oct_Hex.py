number = int(input())

Binary = bin(number)
Octal = oct(number)
Hex = hex(number)

print((Binary)[2:])
print((Octal)[2:])
print((Hex).upper()[2:])