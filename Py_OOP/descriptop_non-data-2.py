from random import choice

class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)

class Game:
    rock = Choice('Rock', 'Paper', 'Scissors')
    flip = Choice('Heads', 'Tails')
    dice = Choice(1, 2, 3, 4, 5, 6)

g = Game()