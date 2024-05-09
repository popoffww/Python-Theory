from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SimpleKivy(App):
    def build(self):
        box = BoxLayout()
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')
        box.add_widget(button1)
        box.add_widget(button2)
        return box


if __name__ == '__main__':
    SimpleKivy().run()
