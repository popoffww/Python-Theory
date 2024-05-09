from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 400)

class CalculatorApp(App):

    def add_number(self, instance):
        if(self.calculate == '0'):
            self.calculate = ''

        self.calculate += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.calculate += str(instance.text)   # if(str(instance.text).lower() == 'x'):
        self.update_label()                    #     self.calculate += '*'
                                               # else:
                                               #     self.calculate += str(instance.text)
    def update_label(self):
        self.label.text = self.calculate

    def result(self, instance):
        self.label.text = str(eval(self.label.text))
        self.calculate = '0'

    def build(self):
        self.calculate = '0'

        boxlayout = BoxLayout(orientation='vertical')
        self.label = (Label(text='0', font_size=40, size_hint=(1, .4), halign='right', valign='middle', text_size=(350,350)))
        boxlayout.add_widget(self.label)

        gridlayout = GridLayout(cols=4, size_hint=(1, .6))
        gridlayout.add_widget(Button(text='7', on_press=self.add_number))
        gridlayout.add_widget(Button(text='8', on_press=self.add_number))
        gridlayout.add_widget(Button(text='9', on_press=self.add_number))
        gridlayout.add_widget(Button(text='+', on_press=self.add_operation))
        gridlayout.add_widget(Button(text='4', on_press=self.add_number))
        gridlayout.add_widget(Button(text='5', on_press=self.add_number))
        gridlayout.add_widget(Button(text='6', on_press=self.add_number))
        gridlayout.add_widget(Button(text='-', on_press=self.add_operation))
        gridlayout.add_widget(Button(text='1', on_press=self.add_number))
        gridlayout.add_widget(Button(text='2', on_press=self.add_number))
        gridlayout.add_widget(Button(text='3', on_press=self.add_number))
        gridlayout.add_widget(Button(text='*', on_press=self.add_operation))
        gridlayout.add_widget(Button(text='0', on_press=self.add_number))
        gridlayout.add_widget(Button(text='.', on_press=self.add_number))
        gridlayout.add_widget(Button(text='=', on_press=self.result))
        gridlayout.add_widget(Button(text='/', on_press=self.add_operation))

        boxlayout.add_widget(gridlayout)

        return boxlayout

if __name__ == '__main__':
    CalculatorApp().run()
