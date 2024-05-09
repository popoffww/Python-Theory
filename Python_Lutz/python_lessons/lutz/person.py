class Person:
    def __init__(self, name='', job='', pay=0):
        self.name=name
        self.job=job
        self.pay=pay

    def people(self):
        print(self.name, self.job, self.pay)

alan = Person()
alan.name = 'Alan Smithee:'
alan.job = 'Software,'
alan.pay = 20000

john = Person()
john.name = 'John Doe:'
john.job = 'Hardware,'
john.pay = 30000

alan.people()
john.people()
