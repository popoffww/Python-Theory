from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SomeBoxLayout(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return SomeBoxLayout()

if __name__ == '__main__':
    MainApp().run()
