from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from GraphicClient.ConfigGraphic import *


class GeoFenceButton(Button):
    _anchor = {'x': 0.5, 'y': 0.5}
    _normalPressImage = None
    _isSwallow = True
    _downPressImage = None
    _defaultSize = None

    def __init__(self, **kwargs):
        super(GeoFenceButton, self).__init__(**kwargs)
        self._defaultSize = self.size_hint

    def checkIsTouchMe(self, touch):
        pos = touch.pos
        print(pos, self.pos, self.size)
        if pos[0] <= self.pos[0] + self.size[0] and pos[0] >= self.pos[0] and pos[1] <= self.pos[1] + self.size[1] and pos[1] >= self.pos[1]:
            print('co return true ko nhi')
            return True
        return False 

    def setContentSize(self, width, height):
        self.size_hint = (width / SIZE_WIDTH, height / SIZE_HEIGHT)
        self._defaultSize = self.size_hint

    def setPosition(self, x, y):
        if self._anchor == None:
            return
        
        pos_hint = { 'x': x / SIZE_WIDTH - self._anchor['x'] * self.size_hint[0], 'y': y / SIZE_HEIGHT - self._anchor['y'] * self.size_hint[1]}
        self.pos_hint = pos_hint

    def setAnchorPoint(self, x, y):
        self._anchor['x'] = x
        self._anchor['y'] = y
        

    def update_child_position(self):
        for c in self.children:
            if isinstance(c, Image):
                c.center = self.center

    def setNormalPressImage(self, path):
        self.background_color = (0, 0, 0, 0)
        if self._normalPressImage == None:
            self._normalPressImage = Image(source = path)
            self.add_widget(self._normalPressImage)

    def setDownPressImage(self, path):
        if self._downPressImage == None:
            self._downPressImage = Image(source = path)
            self.add_widget(self._downPressImage)
        self._downPressImage.opacity = 0
        
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        ret = super(GeoFenceButton, self).on_touch_down(touch)
        # check xem vị trí touch có phải là vị trí của button không
        if not ret:
            return ret
        
        # set lại ảnh khi touch down
        if self._downPressImage != None:
            self._downPressImage.opacity = 0
        if self._normalPressImage != None:
            self._normalPressImage.opacity = 1.0

        return ret

    def on_touch_up(self, touch):
        if self.opacity == 0:
            return False
        ret = super(GeoFenceButton, self).on_touch_up(touch)
        if not ret:
            return ret

        if self._downPressImage != None:
            self._downPressImage.opacity = 0
        if self._normalPressImage != None:
            self._normalPressImage.opacity = 1.0

        return ret
        
