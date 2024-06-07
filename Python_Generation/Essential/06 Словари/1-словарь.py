# Имена всех пользователей(в алфавитном порядке), чей номер оканчивается на 8
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

user = [i['name'] for i in users if i['phone'][-1] == '8']
print(*sorted(user))

# Имена всех пользователей(в алфавитном порядке), у которых нет информации об электронной почте
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

user = [i['name'] for i in users if 'email' not in i or i['email'] == '']
print(*sorted(user))


# Строковое представление
# Числа буквами
n = input()

numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
           '9': 'nine'}

for i in n:
    print(numbers[i], end=' ')


# Напишите программу, которая по номеру курса выводит информацию о данном курсе
string = input().split()

info = {
    'CS101': '3004, Хайнс, 8:00',
    'CS102': '4501, Альварадо, 9:00',
    'CS103': '6755, Рич, 10:00',
    'NT110': '1244, Берк, 11:00',
    'CM241': '1411, Ли, 13:00',
}

for key in string:
    print(key, info[key], sep=': ', end=' ')
# или
my_dict = {
    'CS101': ('3004', 'Хайнс', '8:00'),
    'CS102': ('4501', 'Альварадо', '9:00'),
    'CS103': ('6755', 'Рич', '10:00'),
    'NT110': ('1244', 'Берк', '11:00'),
    'CM241': ('1411', 'Ли', '13:00'),
}

course_number = input()
audience, teacher, time = my_dict[course_number]
print(f'{course_number}: {audience}, {teacher}, {time}')


# Набор сообщений
text = input().upper()

keyboard = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111', '"': '',
            "A": '2', "B": '22', "C": '222',
            "D": '3', "E": '33', "F": '333',
            "G": '4', "H": '44', "I": '444',
            "J": '5', "K": '55', "L": '555',
            "M": '6', "N": '66', "O": '666',
            "P": '7', "Q": '77', "R": '777', "S": '7777',
            "T": '8', "U": '88', "V": '888',
            "W": '9', "X": '99', "Y": '999', "Z": '9999',
            " ": '0'
            }

for key in text:
    print(keyboard[key], end='')
# или
my_dict = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' ',
}

# принимаем строку и сразу преобразуем её в верхний регистр
s = input().upper()

# идём по всем символам строки
for c in s:
    # идём по всем цифрам и значениям для них в словаре
    for digit, values in my_dict.items():
        if c in values:
            # ищем, сколько раз нам надо нажать эту цифру
            cnt = values.index(c) + 1
            print(cnt * digit, end='')
            break


# Код Морзе
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

s = input().upper()

morse_dict = dict(zip(letters, morse))

for key in s:
    if key in morse_dict:
        print(morse_dict[key], end=' ')

# или
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
n = input().upper().replace(" ","")
for i in n:
    if i in letters:
        a = letters.index(i)
        print(morse[a],end=" ")