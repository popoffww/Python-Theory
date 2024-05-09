m = [[1,2,3],[4,5,6],[7,8,9]]
col1 = [row[1] for row in m]
print(col1)

col0 = [row[1] - 1 for row in m]
print(col0)

col_even = [row[2] for row in m if row[2] %2 == 0]
print(col_even)

diag = [m[i][i] for i in(0,1,2)]
print(diag)

doubles = [i*2 for i in m]
print(doubles)

g = (sum(row) for row in m)
print(next(g),next(g),next(g))

s = list(map(sum, m))
print(s)
set = {sum(row) for row in m}
print(set)

set1 = {i:sum(m[i]) for i in range(3)}
print(set1)
ord1 = {i:ord(i) for i in 'spaam'}
print(ord1)

ord2 = [ord(i) for i in 'spaam']
ord3 = {ord(i) for i in 'spaam'}
print(ord2,'\n',ord3)

def gen():
    yield('Never seen a game of T20 cricket?')
    yield ('Where have you been?')
    yield ('So, here\'s a simple explanation \nof what you\'ll be watching \neither at the ground or TV \nthis summer.')

g=gen()
print(g.__next__())
print(g.__next__())
print(g.__next__())

l=[3,5,7,9,2]
it=iter(l)
while True:
    try:
        l=next(it)
        print(l)
    except StopIteration:
        break
