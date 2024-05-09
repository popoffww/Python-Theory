from time import time

class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())

class Time:
    epoch = Epoch()

t = Time()