from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Authorize(GridLayout):
    def __init__(self, **kwargs):
        super(Authorize, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Логин', font_size=20))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Email', font_size=20))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text='Пароль', font_size=20))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)

        self.submit = Button(text='Войти', font_size=30, size_hint=(1,0.2))
        self.submit.bind(on_press=self.mouse_press)
        self.add_widget(self.submit)

    def mouse_press(self, instance):
        name = self.name.text
        email = self.email.text
        password = self.password.text

        print('Логин: ', name, 'Адрес: ', email, 'Пароль: ', password)

class AuthorizeApp(App):
    def build(self):
        return Authorize()

if __name__ == '__main__':
    AuthorizeApp().run()
