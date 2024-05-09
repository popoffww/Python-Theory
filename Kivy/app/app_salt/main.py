from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
# from kivy.config import Config  # расскомментировать для apk-файла
# Config.set('kivy', 'keyboard_mode', 'systemanddock')  # вызов мобильной клавиатуры

Window.size = (480, 640)

def get_ingridients(m):
    salt = str(15 * m / 1000)
    nitro = str(10 * m / 1000)
    zucker = str(5 * m / 1000)
    starts = str(0.5 * m / 1000)
    salting_time = str(round(m / 500 * 2))

    return {'nitro': nitro, 'salt': salt,
    'starts': starts, 'sugars': zucker, 'time':  salting_time}

class Container(GridLayout):
    def calculate(self):
         try:
             mass = int(self.text_input.text)
         except:
             mass = 0

         ingridients = get_ingridients(mass)

         self.salt.text = ingridients.get('salt')
         self.nitro.text = ingridients.get('nitro')
         self.sugars.text = ingridients.get('sugars')
         self.starts.text = ingridients.get('starts')
         self.time.text = ingridients.get('time')

class SaltingApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    SaltingApp().run()
