# Подстрока из списка
def ignore_command(command):
    def ignore_command(command):
        ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
        return any(filter(lambda x: x in command, ignore))

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))



# <capital> is the capital of <country>, population equal <population> people
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for city, state, pop in zip(capitals, countries, population):
    print(f'{city} is the capital of {state}, population equal {pop} people.')


# Внутри шара
abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, zip(abscissas, ordinates, applicates))))


# Корректный IP-адрес
print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split('.'))))


# Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне a-b,
# которые делятся на каждую содержащуюся в них цифру без остатка
a, b = int(input()), int(input())

for i in range(a, b + 1):
    nums = [int(j) for j in str(i)]
    if all(map(lambda x: x != 0 and i % x == 0, nums)):
        print(i, end=' ')


# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов,
# содержит хотя бы одну цифру, заглавную и строчную букву
s = input()

print('YES' if all((any(i.isdigit() for i in s),
                    any(i.islower() for i in s),
                    any(i.isupper() for i in s),
                    len(s) >= 7)) else 'NO')

# Отличники
students = []

for i in range(int(input())):
    students.append(any(['5' in input() for j in range(int(input()))]))

print('YES' if all(students) else 'NO')