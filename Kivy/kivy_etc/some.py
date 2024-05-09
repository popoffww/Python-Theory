from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'width', 288)
Config.set('graphics', 'height', 512)

class MainWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class ManagerWindow(ScreenManager):
    pass

app_some = Builder.load_file('some.kv')

class SomeApp(App):

    def build(self):
        return app_some


if __name__ == '__main__':
    SomeApp().run()
