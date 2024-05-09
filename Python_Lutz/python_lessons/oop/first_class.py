
class Employee:
    def __init__(self,name='',age=0,pay=0,job=''):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def people(self):
        print(self.name, self.age, self.pay, self.job)

alan = Employee()
alan.name = 'Alan Smithee:'
alan.age = 42
alan.pay = 30000
alan.job = 'software'
jane = Employee()
jane.name = 'Jane Doe:'
jane.age = 45
jane.pay = 45000
jane.job = 'hardware'

Employee.people(alan)
jane.people()

