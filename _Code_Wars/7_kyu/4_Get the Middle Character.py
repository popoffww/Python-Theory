def get_middle(s):

    if len(s) % 2 != 0:
        return s[len(s) // 2]

    elif len(s) % 2 == 0:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]

    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]

print(get_middle("test"),"es")
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")

def get_middle(s):

    while len(s) > 2:
        s = s[1:-1]

    return s