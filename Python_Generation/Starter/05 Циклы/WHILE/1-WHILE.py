# До КОНЦА
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()


text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()

text = input()
while not (text == "КОНЕЦ" or text == "конец"):
    print(text)
    text = input()


# Количество строк
text = input()
counter = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    counter += 1
    text = input()
print(counter)


# Пока делимся на 7
number = int(input())
while number % 7 == 0:
    print(number)
    number = int(input())


# Сумма чисел
number = int(input())
total = 0
while number >= 0:
    total += number
    number = int(input())
print(total)


# Количество пятерок
number = int(input())
total = 0
while 0 < number <= 5:
    if number == 5:
        total += 1
    number = int(input())
print(total)


# В мире Ведьмака существуют монеты с номиналами 1, 5, 10, 25:
# какое минимальное количество чеканных монет нужно заплатить Ведьмаку
number = int(input())
counter = 0

while number != 0:
    if number >= 25:
        number -= 25
        counter += 1
    elif number >= 10:
        number -= 10
        counter += 1
    elif number >= 5:
        number -= 5
        counter += 1
    elif number >= 1:
        number -= 1
        counter += 1
print(counter)