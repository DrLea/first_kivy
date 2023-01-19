from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from random import randint

class MyWidjet(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(randint(1, 100)/100, randint(1, 100)/100, randint(1, 100)/100)
            touch.ud["line"] = Line(points = (touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)


class MyApp(App):
    def build(self):
        return MyWidjet()

if __name__=="__main__":
    MyApp().run()