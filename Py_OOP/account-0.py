from datetime import datetime
import pytz

WHITE = '\033[00m'
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'

# WHITE = '\033[00m'
# RED = '\033[41m'
# GREEN = '\033[42m'
# CYAN = '\033[46m'

class Account:
    def __init__(self, name, __balance):
        self.name = name
        self.__balance = __balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        print(f'Вы внесли {amount} рублей')
        self.show___balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'Вы вывели {amount} рублей')
            self.show___balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print('Недостаточно средств')
            self.show___balance()

    def show___balance(self):
        print(f'Баланс: {self.__balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'Внесено'
                color = GREEN
            else:
                transaction = 'Снято'
                color = RED
            print(f'{color} {transaction} {amount} {CYAN} на {date.astimezone()}')

a = Account("User", 0)

a.deposit(1580)
a.deposit(540)
a.deposit(360)
a.withdraw(150)
a.withdraw(890)
a.show_history()


