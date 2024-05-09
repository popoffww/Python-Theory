from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        root = Widget()
        root.add_widget(Button())
        slider = Slider()
        root.add_widget(slider)

        return root

if __name__ == '__main__':
    MainApp().run()
