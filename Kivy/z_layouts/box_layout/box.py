from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Box(BoxLayout):
    def __init__(self, **kwargs):
        super(Box, self).__init__(**kwargs)

        self.cols = 2
        self.layout = BoxLayout(orientation='vertical')
        self.btn1 = Button(text='Hello')
        self.btn2 = Button(text='World')
        self.layout.add_widget(self.btn1)
        self.layout.add_widget(self.btn2)

class MainApp(App):
    def build(self):
        return Box()

if __name__ == '__main__':
    MainApp().run()
