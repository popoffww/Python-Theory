my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {key: [i for i in my_dict[key] if i <= 20] for key in my_dict}
print(my_dict)

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

result = sorted({i + '@' + key for key, value in emails.items() for i in value})
print(*result, sep='\n')


# Минутка генетики
my_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

result = [my_dict[i] for i in input()]

print(*result, sep='')


# Порядковый номер
s = input().split()

result = {}

for i in s:
    result[i] = result.get(i, 0) + 1
    print(result[i], end=' ')


# Scrabble game
# Общая стоимость слова – сумма баллов его букв
my_dict = {
    1: 'AEILNORSTU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ',
}

s = input()

result = [key for letter in s for key, value in my_dict.items() if letter in value]

print(sum(result))


# Строка запроса
def build_query_string(params):
    return '&'.join([f'{key}={value}' for key, value in sorted(params.items())])


# Слияние словарей
# Следующий программный код:
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# создает словарь:
# result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
def merge(values):      # values - это список словаре
    result = {}
    for d in values:
        for key in d:
            result.setdefault(key, set()).add(d[key])

    return result


# Опасный вирус
result = {}

d = {'W': 'write', 'R': 'read', 'X': 'execute'}

for _ in range(int(input())):
    x = input().split()
    result[x[0]] = [d[i] for i in x[1:]]

for _ in range(int(input())):
    x = input().split()
    if x[0] in result[x[1]]:
        print('OK')
    else:
        print('Access denied')


# Покупки в интернет-магазине
result = {}

for _ in range(int(input())):
    name, product, count = input().split()
    result.setdefault(name, {})
    result[name][product] = result[name].get(product, 0) + int(count)

for key, value in sorted(result.items()):
    print(f'{key}:')
    for i in sorted(value):
        print(i, value[i])