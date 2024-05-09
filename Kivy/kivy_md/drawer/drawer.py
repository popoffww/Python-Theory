from kivy.app import App
from kivymd.theming import ThemeManager

class DrawerApp(App):
    theme_cls = ThemeManager()

DrawerApp().run()
