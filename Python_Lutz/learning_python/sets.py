a = {1,2,3,4,5}
b = {2,5,6}
print('Пересечение(&):', a & b)
c = a.intersection(b)
print('Intersection/Пересечение(&):',c)

print('Объединение(|):', a | b)
c.update(a,b)
print('Update/Объединение(|):', c)
print('Симметрическая разность:',a ^ b)
print('Симметрическая разность:',b ^ a)
print(a - b)
print(b - a)