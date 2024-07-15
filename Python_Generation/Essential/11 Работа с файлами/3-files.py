import random
# Напишите программу, которая считывает строку текста и записывает её в текстовый файл
with open('output.txt', 'w') as output:
    print(input(), file=output)


# Случайные числа
with open('random.txt', 'w') as output:
    for _ in range(25):
        print(random.randrange(111, 777), sep='\n', file=output)
# или
with open('random.txt', 'w', encoding='utf-8') as file:
    for _ in range(25):
        file.write(str(random.randint(111, 777)) + '\n')


# Нумерация строк
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
with open('input.txt', encoding='utf-8') as output:
    lst = [str(i) + ') ' + line for i, line in enumerate(output, 1)]

with open('output.txt', 'w', encoding='utf-8') as output:
    output.writelines(lst)


# Напишите программу для добавления 5 баллов к каждому результату теста
# и вывода фамилий и новых результатов тестов в новый файл
# Если бы файл class_scores.txt содержал строки:
# Washington 83
# Adams 86
# Kingsman 100
# MacDonald 95
# Thomson 98
# то файл new_scores.txt имел бы вид:
# Washington 88
# Adams 91
# Kingsman 100
# MacDonald 100
# Thomson 100
with open('class_scores.txt', encoding='utf-8') as class_scores, open('new_scores.txt', 'w',
                                                                      encoding='utf-8') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100

        print(name, score, file=new_scores)


# Загадка от Жака Фреско
# goats.txt
# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat
with open('goats.txt', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as answer:
    x = file.read().split('GOATS')
    colors = x[0].split('\n')[1:]
    goats = x[1].split('\n')

    for line in colors:
        if goats.count(line) > len(goats) * 0.07:
            answer.write(line + '\n')


# Конкатенация файлов
with open('output.txt', 'a', encoding='utf-8') as output:
    for _ in range(int(input())):
        with open(input(), encoding='utf-8') as file:
            output.write(file.read())


# Лог файл
# Если бы файл logfile.txt содержал строки:
# Тимур Гуев, 14:10, 15:50
# Руслан Гриценко, 12:00, 12:59
# Роман Гацалов, 09:10, 17:45
# Габолаев Георгий, 11:10, 12:10
# то файл output.txt имел бы вид:
# Тимур Гуев
# Роман Гацалов
# Габолаев Георгий
with open('logfile.txt', encoding='utf-8') as info, open('output.txt', 'w', encoding='utf-8') as logs:
    for line in info:
        name, entry, exit = line.strip().split(', ')
        if (int(exit[:2]) * 60 + int(exit[3:])) - (int(entry[:2]) * 60 + int(entry[3:])) >= 60:
            print(name, file=logs)