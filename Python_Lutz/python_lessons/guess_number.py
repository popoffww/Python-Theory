
import random

def guess(span):
    number = random.randint(1,span)  #random.randrange(1,span)
    while True:
        print('\tУгадайте число от 1 до {}'.format(span))
        input_number = int(input('\tВведите число: '))
        if  input_number == number:
            print('\tВы угадали.')
            break
        elif input_number < number:
            print('\tЗагаданное число больше')
        else:
            print('\tЗагаданное число меньше')

for _ in range(10,40,10):
    guess(_)

print("""\tВы победили!
\tНо приза не будет.
\tДенег нет(((
""")

