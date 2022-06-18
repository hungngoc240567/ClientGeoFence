from faulthandler import disable
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Point, Line
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapSource
from kivy.graphics.instructions import InstructionGroup
from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import ObjectProperty
from GraphicClient.ConfigGraphic import SIZE_HEIGHT, SIZE_WIDTH
from GraphicClient.GUILayer import *
from kivy.core.window import Window
from GraphicClient.GeoFenceMapView import *
from Vehicle.VehicleManager import *
from GeoFence.GeoFenceManager import *
from GraphicClient.AppClient import *


geoFenceMgr = GeoFenceManager()
GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_CONTROLLER'] = geoFenceController
GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER'] = geoFenceMgr
GLOBAL_GRAPHIC_VARIABLE['VEHICLE_MANAGER'] = VehicleManager()
class MyAppTest(App):

    def onUserStartDrawGeoFence(self):
        self.mapView.onUserStartDrawGeoFence()

    def onUserFinishDrawGeoFence(self):
        self.mapView.onUserFinishDrawGeoFence()

    def onUserEnterGeoFence(self):
        listSendPoint = self.mapView.onUserEnterGeoFence()
        geoFenceMgr.addGeoFenceByListPoint(listSendPoint)
        self.mapView.do_update(0)

    def getListGeoFence(self):
        return geoFenceMgr.getListGeoFence()
    
    def onUserDenyGeoFence(self):
        return

    def build(self):
        self.layout = FloatLayout(size = Window.size)
        self.mapView = GeoFenceMapView(zoom=11, lat=50.6394, lon=3.057)
        GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW'] = self.mapView
        self.mapView.setGUIControl(self)
        self.guiLayer = GUILayer()
        self.guiLayer.setControlGUI(self)
        self.objectDrawTouch = GeoFenceTouchDraw(size = (SIZE_WIDTH, SIZE_HEIGHT))
        GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW'] = self.objectDrawTouch
        GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_GUI_LAYER'] = self.guiLayer
        self.layout.add_widget(self.objectDrawTouch, index = 0)
        self.layout.add_widget(self.guiLayer, index = 2)
        self.layout.add_widget(self.mapView, index = 3)
        return self.layout

MyAppTest().run()