from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        # layout = BoxLayout(orientation='vertical')
        # btn1 = Button(text='Hello')
        # btn2 = Button(text='World')
        # layout.add_widget(btn1)
        # layout.add_widget(btn2)
        layout = BoxLayout(orientation='vertical', spacing=5)
        # btn1 = Button(text='Hello', size_hint=(1, .7))
        # btn2 = Button(text='World', size_hint=(1, .3))
        btn1 = Button(text='Hello', size=(200, 100), size_hint=(None, None))
        btn2 = Button(text='Kivy', size_hint=(.5, 1))
        btn3 = Button(text='World', size_hint=(1, .5))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

if __name__ == '__main__':
    MainApp().run()
