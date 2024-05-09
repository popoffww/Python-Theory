from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Box(BoxLayout):
    pass

class BoxApp(App):
    def build(self):
        return Box()

if __name__ == '__main__':
    BoxApp().run()
