m = []
for i in range(20):
    m.append(str(i))
    # ''.join(m)
print(m)
str = ''.join(m)
print(str)

s='abcndefghij'
print(s)
w=s.find('nde')
s=s[:w]+'xyz'
print(s)
l=list(s)
print(l)
s=''.join(l)
s='|'.join(l)
print(s)

s='s,pa,m'
print(len(s))
print(s[2:4])
s1=s.split(',')
print(s.split(','))
print(len(s1))
print(s.split(',')[1])

st=['a','A','Z','z']
st.sort(key=str.casefold)
print(st)
