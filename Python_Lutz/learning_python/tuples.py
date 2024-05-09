c = ('Pythonville', 'Spamburg', 'Eggstown')
p = (10000, 20000, 30000)
z=zip(c, p)
print(z)
l=list(enumerate(z))
print(l)

L = list(zip(['1', '2', '3'], ['Bowled', 'Run Out', 'Stumped']))
print(L)

d = dict(zip(['1', '2', '3'], ['Bowled', 'Run Out', 'Stumped']))
print(d)
