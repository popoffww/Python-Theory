from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
    #     self.cols = 2
    #
    #     self.add_widget(Label(text='Логин:'))
    #     self.username = TextInput(multiline=False)
    #     self.add_widget(self.username)
    #
    #     self.add_widget(Label(text='Пароль:'))
    #     self.password = TextInput(multiline=False)
    #     self.add_widget(self.password)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
