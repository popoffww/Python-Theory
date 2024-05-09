from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainFood(Screen):
    pass

class AddFood(Screen):
    pass

class ListFood(Screen):
    pass

class ManagerFood(ScreenManager):
    pass

app_food = Builder.load_file('food.kv')

class FoodApp(App):
    def build(self):
        return app_food

if __name__ == '__main__':
    FoodApp().run()
