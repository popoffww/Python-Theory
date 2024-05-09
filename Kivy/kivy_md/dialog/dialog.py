from kivy.app import App
from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.theming import ThemeManager

class DialogApp(App):
    theme_cls = ThemeManager()
    def show_MDDialog(self):
        my_dialog = MDDialog(title='Диалоговое окно', text='Здесь могла бы быть ваша реклама',
                             size_hint=[.5, .5], auto_dismiss=False,
                             events_callback=self.my_callback, text_button_ok='Согласен', text_button_cancel='Не согласен')
        my_dialog.open()

    def my_callback(self, text_of_selection, popup_widget):
        print(text_of_selection)
        print(popup_widget)
        print(popup_widget.text_field.text)

    def show_MDInputDialog(self):
        my_dialog = MDInputDialog(title='Поле ввода', hint_text='Ввести здесь',
                                  size_hint=[.5, .5], auto_dismiss=False,
                                  events_callback=self.my_callback, text_button_ok='Согласен')
        my_dialog.open()

DialogApp().run()
