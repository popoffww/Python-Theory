from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# округление до первого знака после запятой
map_result = list(map(lambda num: round(num ** 2, 1), floats))
# палиндромы длиною больше 4-х символов
filter_result = list(filter(lambda w: len(w) > 4 and w == w[::-1] , words))
# произведение
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)

# Список primary городов с населением более 10_000_000
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

capitals = filter(lambda data: data[2] == 'primary' and data[1] > 10_000_000, data)
capitals = map(lambda data: data[0], capitals)
capitals = sorted(capitals)
capitals = 'Cities: ' + reduce(lambda caps_1, caps_2: f'{caps_1}, {caps_2}', capitals)
print(capitals)