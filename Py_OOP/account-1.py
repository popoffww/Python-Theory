from datetime import datetime
import pytz

# WHITE = '\033[00m'
# RED = '\033[31m'
# GREEN = '\033[32m'
# CYAN = '\033[36m'

WHITE = '\033[00m'
RED = '\033[41m'
GREEN = '\033[42m'
CYAN = '\033[46m'


class Account:
    def __init__(self, name, __balance):
        self.name = name
        self.__balance = __balance
        self.history = []
        
    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        print(f'На счет поступило {amount} рублей')
        self.show___balance() 
        self.history.append([amount, self._current_time()])
                      
    def spent(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'Со счета выведено {amount} рублей')
            self.show___balance()
            self.history.append([-amount, self._current_time()])
        else:
            print('Недостаточно средств')
            
    def show___balance(self):
        print(f'Баланс: {self.__balance}')
    
    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'Поступило'
                color = GREEN
            else:
                transaction = 'Выведено'
                color = RED
            print(f'{color} {transaction} {amount} на {CYAN} {date.astimezone()}')
            
a = Account('User', 0)

a.deposit(100)
a.spent(50)
a.show_history()

print(datetime.now())
