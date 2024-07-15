import string

def high(x):

    alphabet = string.ascii_lowercase
    dct = {}
    for i in x.split():
        dct[i] = sum(alphabet.index(x) + 1 for x in i)

    return max(dct.items(), key=lambda x: x[1])[0]

print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')
print(high('aa b'), 'aa')
print(high('b aa'), 'b')
print(high('bb d'), 'bb')
print(high('d bb'), 'd')
print(high("aaa b"), "aaa")

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c) - 96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word



def high(x):

    maxValue = -1;
    maxWord = "";

    values = {'a':1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
                'o':15, 'p':16, 'q':17, 'r':18, 's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

    words = x.split();

    for word in words:

        currentSum = 0;

        for char in word:

            currentSum += values[char];

        if currentSum > maxValue:
            maxValue = currentSum;
            maxWord = word;

    return maxWord;