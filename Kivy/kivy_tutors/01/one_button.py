from kivy.app import App
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass


class OneButton(App):
    def build(self):
        return Widgets()

if __name__ == '__main__':
    OneButton().run()
