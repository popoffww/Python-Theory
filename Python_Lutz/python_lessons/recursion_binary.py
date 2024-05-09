
def converter(n):
    b = n % 2
    if n >= 2:
        converter(n/2)
    print(b)

n = int(input('Введите число: '))
converter(n)