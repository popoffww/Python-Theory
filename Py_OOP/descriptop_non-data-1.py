from random import choice

class Game:
    @property
    def rock(self):
        return choice(['Rock', 'Paper', 'Scissors'])

    @property
    def flip(self):
        return choice(['Heads', 'Tails'])

    @property
    def dice(self):
        return choice(range(1, 7))

g = Game()

# in console:
# for i in range(3):
# print(g.dice)

