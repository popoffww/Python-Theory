import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class PasswordApp(App):

    def get_password(self, instance):
        def create_password(self, *args):

            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            length = pass_new
            password = ''

            for i in range(length):
                password += random.choice(chars)

            return {'password': password}

        try:
            pass_new = int(self.input.text)
        except:
            pass_new = 0

        password_ = create_password(pass_new)

        self.label_get.text = password_.get('password')

    def build(self):

        main_boxlayout = BoxLayout(orientation='vertical')

        top_boxlayout = BoxLayout(orientation='vertical', padding=[0,20,0,70])
        self.label_number = Label(text='Введите число символов пароля', font_size=20)
        top_boxlayout.add_widget(self.label_number)
        self.input = TextInput(multiline=False, input_type='number', input_filter='int', font_size=30, size_hint=(1,.6))
        top_boxlayout.add_widget(self.input)

        button_boxlayout = BoxLayout(orientation='vertical', padding=[100,0,100,50], size_hint=(1,.5))
        self.button = Button(text='Создать пароль', font_size=20, on_release=self.get_password)
        button_boxlayout.add_widget(self.button)

        bottom_boxlayout = BoxLayout(orientation='vertical', padding=[0,20,0,60], spacing=40)
        self.label_new = Label(text='Новый пароль', font_size=30)
        self.label_get = Label(text='0', font_size=30)
        bottom_boxlayout.add_widget(self.label_new)
        bottom_boxlayout.add_widget(self.label_get)

        main_boxlayout.add_widget(top_boxlayout)
        main_boxlayout.add_widget(button_boxlayout)
        main_boxlayout.add_widget(bottom_boxlayout)

        return main_boxlayout

if __name__ == '__main__':
    PasswordApp().run()
