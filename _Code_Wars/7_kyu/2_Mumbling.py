def accum(st):

    return '-'.join((a * i).title() for i, a in enumerate(st, 1))

print(accum("ZpglnRxqenU"),
"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
print(accum("NyffsGeyylB"),
"N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
print(accum("MjtkuBovqrU"),
"M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
print(accum("EvidjUnokmM"),
"E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
print(accum("HbideVbxncC"),
"H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")


def accum(st):
    i = 0
    result = ''
    for letter in st:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]


def accum(st):
    index = 1
    result = []
    for letter in st:
        letter *= index
        letter = letter.capitalize()
        index += 1
        result.append(letter)
    return '-'.join(result)