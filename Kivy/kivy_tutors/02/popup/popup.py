from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class AddLocationForm(BoxLayout):
    pass


class TestApp(App):
    def build(self):

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text='Получено новое сообщение'))
        button = Button(text='Закрыть')
        layout.add_widget(button)
        popup = Popup(title='Уведомление', content=layout)
        button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    TestApp().run()
