from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class GeoFenceDialog(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text = "")
        self.add_widget(self.label)

    def setString(self, str):
        self.label.text = str
    
