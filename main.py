from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="Button1")
        b2 = Button(text="Button2")
        self.add_widget(b2)
        self.add_widget(b1)"""


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
