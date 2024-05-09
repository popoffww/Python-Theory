from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory


class WeatherRoot(BoxLayout):
    def show_current_weather(self, location):
        self.clear_widgets()
        current_weather = Factory.CurrentWeather()

        current_weather.location = location
        self.add_widget(current_weather)

class WApp(App):
    def build(self):
        return WeatherRoot()

if __name__ == '__main__':
    WApp().run()
