class Name:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = '{}'.format(self._name) + ' ' + '{}'.format(self._surname)
        return self._full_name

n = Name('Gordon', 'Shumway')


# getattr(Name,'name')
# setattr(Name, 'name', 'Tom')


