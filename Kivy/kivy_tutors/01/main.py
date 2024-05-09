from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Container(GridLayout):
    def change_text(self):
        abracadabra = ObjectProperty()
        label_text = ObjectProperty()
        self.label_text.text = self.abracadabra.text.upper()

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
