from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class FactBoxLayout(BoxLayout):

    def get_factorial(self):

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        n = int(self.display.text)
        f = factorial(n)
        self.result.text = factorial(f)

class FactorialApp(App):
    def build(self):
        return FactBoxLayout()

if __name__ == '__main__':
    FactorialApp().run()
