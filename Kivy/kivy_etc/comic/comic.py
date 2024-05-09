from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ComicBoxLayout(BoxLayout):
    pass

class ComicApp(App):
    def build(self):
        return ComicBoxLayout()

if __name__ == '__main__':
    ComicApp().run()
