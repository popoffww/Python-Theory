class Animal():
    def __init__(self):
        self.run = False
        self.fly = False

    def possible(self):
        print(type(self).__name__, ':')
        print('Can run:', self.run)
        print('Can fly:', self.fly)
        print('* ' * 8)


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.run = True


class Bird(Animal):
    def possible(self):
        super().possible()
        self.fly = True


class Pegasus(Horse, Bird):
    pass


if __name__ == '__main__':
    horse = Horse()
    horse.possible()

    bird = Bird()
    bird.possible()

    pegasus = Pegasus()
    pegasus.possible()

for i in [Animal, Horse, Bird, Pegasus]:
    print(i.__mro__)
print(Pegasus.mro())
print('* ' * 8)
print(isinstance(bird, Horse))
print(issubclass(Animal, Horse))
print(isinstance(pegasus, Bird))
print(issubclass(Pegasus, Animal))


