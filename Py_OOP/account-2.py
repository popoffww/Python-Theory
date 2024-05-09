BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
VIOLET = '\033[35m'

class Wallet:
    def __init__(self, user='Уважаемый клиент', rub='RUB'):
        self.user = user
        self.rub = rub
        self.__money = 0

    def debet(self, amount):
        green = GREEN
        self.__money += amount
        print(f'{green}На счет поступило {amount} {self.rub}')
        self.info()

    def credit(self, amount):
        blue = BLUE
        red = RED
        if self.__money > amount:
            self.__money -= amount
            print(f'{blue}Со счета выведено {amount} {self.rub}')
            self.info()
        else:
            print(f'{red}Недостаточно средств!')

    def deposit(self):
        while True:
            if self.__money == 0:
                print(f"Здравствуйте, {self.user}.\nВас приветствует банк - \n'СтройДроваИнвестЗасол'.'\nНа вашем счете: {self.__money} {self.rub}. Пополните счет.")
                __money_in = int(input('Введите сумму:\n'))
                __money_in = client.debet(__money_in)
                black = BLACK
            choice = int(input(f'''{black}Что вы хотите?
Укажите номер операции:
1. Внести деньги.
2. Снять деньги.
3. Завершить работу.
'''))
            if choice == 1:
                print('Внесите деньги.')
                plus = int(input())
                client.debet(plus)
            elif choice == 2:
                print('Снимите деньги.')
                minus = int(input())
                client.credit(minus)
            elif choice == 3:
                black = BLACK
                print(f'{black}До свидания.\nМы рады, что вы являетесь нашим клиентом.')
                break
            else:
                print('Неправильный ввод.\nПопробуйте еще раз.')

    def info(self):
        violet = VIOLET
        print(f'{violet}Итого на вашем счете: {self.__money} {self.rub}')

client = Wallet()
client.deposit()

