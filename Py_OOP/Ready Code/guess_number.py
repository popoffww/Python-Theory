import random

def guess(span):

    number = random.randint(1, span)

    while True:

        print("\tУгадайте число от 1 до {}".format(span))

        input_number = int(input("\tВведите число: "))

        if input_number == number:

            print("\tПравильно. Оценка 5!")
            print("\t====================")

            break

        elif input_number < number:

            print("\tЗагаданное число больше")

        else:

            print("\tЗагаданное число меньше")


for _ in range(10, 40, 10):

    guess(_)


print(
    """\tИгра окончена.
\tЗа призом приходите завтра.
\tА лучше никогда.
"""
)
