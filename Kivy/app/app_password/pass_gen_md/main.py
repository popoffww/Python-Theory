import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)
from kivymd.theming import ThemeManager

class Container(BoxLayout):
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
    theme_cls = ThemeManager()
    def build(self):
        return Container()

if __name__ == '__main__':
    PasswordApp().run()
