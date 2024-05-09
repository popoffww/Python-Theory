from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawRelativeLayout(RelativeLayout):
    pass
    
class DrawingApp(App):
    def build(self):
        return DrawRelativeLayout()

if __name__=="__main__":
     DrawingApp().run()
