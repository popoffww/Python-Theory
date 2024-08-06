m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

a, b, c = map(int, input().split())

notes = [m[a-1], m[b-1], m[c-1]]

res = ' '.join(notes)

print(res) if 'до' not in res and 'фа' not in res else \
    print(res.replace('до', '#до', 3).replace('фа', '#фа', 3))


# Второй вариант
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

notes = [int(i) - 1 for i in input().split()]

for note in notes:
    print(f'#{m[note]}' if note in [0, 3] else m[note], end=' ')