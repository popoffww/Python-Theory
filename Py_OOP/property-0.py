class Name:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_surname(self):
        return self._surname

    def set_surname(self, value):
        self._surname = value

    def full_name(self):
        return '{}'.format(self._name) + ' ' + '{}'.format(self._surname)

    name = property(fget=get_name, fset=set_name)
    surname = property(fget=get_surname, fset=set_surname)
    full_name = property(fget=full_name)

    # or
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)
    # surname = property()
    # surname = surname.getter(get_surname)
    # surname = surname.setter(set_surname)
    # full_name = property(fget=full_name)

n = Name('Gordon', 'Shamway')