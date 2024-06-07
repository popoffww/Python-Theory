# Получить множество, содержащее цифры из списка
items = [10, '30', 30, 10, '56', 34, '12',
         90, 89, 34, 45, '67', 12, 10, 90,
         23, '45', 56, '56', 1, 5, '6', 5
        ]

my_set = {int(i) for i in items}

print(*sorted(my_set))

# Получить множество, содержащее первую букву (в нижнем регистре) каждого слова списка
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate',
         'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
         'tangerine', 'Watermelon', 'currant', 'Almond'
        ]

words = {i.lower()[0] for i in words}

print(*sorted(words))


# Получить множество, содержащее уникальные (в нижнем регистре) слова строки
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, 
and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and 
dells of memory, over which, if you can still stand my style (I am writing under observation), 
the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, 
with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, 
at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.
'''
my_set = {i.lower().strip('.,;:()') for i in sentence.split()}

print(*sorted(my_set))


# Получить множество, содержащее уникальные слова строки длиною меньше 4 символов
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, 
and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and 
dells of memory, over which, if you can still stand my style (I am writing under observation), 
the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, 
with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, 
at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.
'''
my_set = {i.strip('.,;:()') for i in sentence.lower().split() if len(i.strip('.,;:()')) < 4}

print(*sorted(my_set))


# Выбрать имена файлов c расширением .png, независимо от регистра имен и расширений
files = ['python.png', 'qwerty.py', 'stepik.png',
         'beegeek.org', 'windows.pnp', 'pen.txt',
         'phone.py', 'book.txT', 'board.pNg',
         'keyBoard.jpg', 'Python.PNg', 'apple.jpeg',
         'png.png', 'input.tXt', 'split.pop',
         'solution.Py', 'stepik.org', 'kotlin.ko',
         'github.git'
         ]

my_set = {i.lower() for i in files if i.lower().endswith('.png')}

print(*sorted(my_set))