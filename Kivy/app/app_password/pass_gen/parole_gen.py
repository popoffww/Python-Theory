import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class PassGenGridLayout(GridLayout):
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

class ParoleApp(App):
    def build(self):
        return PassGenGridLayout()

if __name__ == '__main__':
    ParoleApp().run()
