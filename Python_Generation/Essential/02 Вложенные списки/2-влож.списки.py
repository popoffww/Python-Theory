# Построчный список, состоящий из n списков
# Мое решение
array = [i + 1 for i in range(int(input()))]

for li in array:
    print(array)

# Варианты
n = int(input())
for _ in range(n):
    print(list(range(1, n + 1)))

print('=' * n * 3)

result = []
for _ in range(n):
    result.append(list(range(1, n + 1)))
print(*result, sep='\n')

# Построчный список 2, состоящий из n списков
n = int(input())
for i in range(1, n + 1):
    print(list(range(1, i + 1)))

print('=' * n * 3)

# Варианты
result = []
for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))
print(*result, sep='\n')