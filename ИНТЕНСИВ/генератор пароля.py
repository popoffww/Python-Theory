import random
import string

pass_length = int(input())

up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
nums = string.digits
password = ''.join(random.sample((up_letters + low_letters + nums), pass_length))

print(password)


# Генератор паролей 1
# в каждом пароле необязательно должна присутствовать хотя бы одна цифра
# и буква в верхнем и нижнем регистре
def generate_password(length):

    password = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    password = ''.join([sym for sym in password if sym not in 'lIoO'])
    return ''.join(random.sample(password, length))


def generate_passwords(count, length):

    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


# Генератор паролей 2
# в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре
def generate_password(length):

    up = [sym for sym in string.ascii_uppercase if sym not in 'IO']
    low = [sym for sym in string.ascii_lowercase if sym not in 'lo']
    num = list(string.digits[2:])
    sym = up + low + num

    password = [random.choice(i) for i in(up, low, num)]
    password += [random.choice(sym) for i in range(length - 3)]

    return ''.join(password)


def generate_passwords(count, length):

    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


# Kivy password generator
def get_password(self):
    def create_password(self):

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = pass_new
        password = ''

        for i in range(length):
            password += random.choice(chars)

        return {'password': password}

    try:
        pass_new = int(self.display.text)
    except:
        pass_new = 0

    password_ = create_password(pass_new)

    self.result.text = password_.get('password')