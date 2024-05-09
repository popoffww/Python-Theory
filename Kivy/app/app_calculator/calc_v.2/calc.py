from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcBoxLayout(BoxLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = 'Ошибка'

class CalcApp(App):
    def build(self):

        return CalcBoxLayout()

if __name__ == '__main__':
    CalcApp().run()
