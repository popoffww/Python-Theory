class Person:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value= value

    def get(self):
        return self._value

class Name:
    def __init__(self, name, surname):
        self.name = Person(name)
        self.surname = Person(surname)

n = Name('Gordon', 'Shumway')

# in console:
#  n.name.get()
#  n.name.set('John')