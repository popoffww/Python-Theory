import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.config import Config  # расскомментировать для apk-файла
# Config.set('kivy', 'keyboard_mode', 'systemanddock')  # вызов мобильной клавиатуры

class Container(GridLayout):
    def get_password(self):
        def create_password(self):

            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # chars = '+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            length = pass_new
            password = ''

            for i in range(length):
                password += random.choice(chars)

            return {'password': password}

        try:
            pass_new = int(self.txt_prop.text)
        except:
            pass_new = 0

        password_ = create_password(pass_new)

        self.pass_prop.text = password_.get('password')

class PasswordApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    PasswordApp().run()
