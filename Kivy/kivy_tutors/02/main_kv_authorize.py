from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Authorize(Widget):
    login = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print('Login:', self.login.text, 'Email:', self.email.text)


class MainApp(App):
    def build(self):
        return Authorize()

if __name__ == '__main__':
    MainApp().run()
