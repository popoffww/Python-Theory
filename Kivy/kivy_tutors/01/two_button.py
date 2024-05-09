from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatLayouts(FloatLayout):
    pass

class TwoButton(App):
    def build(self):
        return FloatLayouts()

if __name__ == '__main__':
    TwoButton().run()
