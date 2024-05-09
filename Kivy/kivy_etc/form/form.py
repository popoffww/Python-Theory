from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 640)
Config.set('graphics', 'height', 480)


class FormBoxLayout(BoxLayout):
    pass

class FormApp(App):
    def build(self):
        return FormBoxLayout()

if __name__ == '__main__':
    FormApp().run()
