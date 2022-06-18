from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Point, Line
from random import random as r
from functools import partial
# Thay đường dẫn của mọi người đến thư mục này hen
import sys

from numpy import ones_like
sys.path.append('/Users/lap13994/Documents/FinalGeoFenceProject/ClientGeoFence/')
from GraphicClient.VehicleLayout import *
from GraphicClient.GeoFenceLayout import *


class AppGeoFenceClient(App):

    def addGeoFence(self, *largs):
        self.geoFenceMgr.addGeoFence(1)
        self.geoFenceLayout.drawListGeoFence(self.geoFenceMgr)

    def addVehicleX10(self, *largs):
        self.vehicleMgr.addVehicle(10)

    def setInfoMgr(self, geoFenceMgr, vehicleMgr):
        self.geoFenceMgr = geoFenceMgr
        self.vehicleMgr = vehicleMgr

    def updateListGeoFence(self, dt):
        self.geoFenceLayout.drawListGeoFence(self.geoFenceMgr)

    def updateListVihcle(self, dt):
        self.vehicleLayout.drawListVehicle(self.vehicleMgr.getListVehicle(), self.geoFenceMgr)

    def build(self):
        self.drawLayout = FloatLayout()
        self.geoFenceLayout = GeoFenceLayout()
        self.geoFenceLayout.setInit()
        self.vehicleLayout = VehicleLayout()

        self.btnAddGeoFence = Button(text = 'add Geo Fence', on_press = partial(self.addGeoFence))
        self.btnAddVehiclex10 = Button(text = 'add Vehicle x10', on_press = partial(self.addVehicleX10))
        layoutBtn = BoxLayout(size_hint=(1, None), height=50)
        layoutBtn.add_widget(self.btnAddGeoFence)
        layoutBtn.add_widget(self.btnAddVehiclex10)

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.drawLayout)
        self.drawLayout.add_widget(self.geoFenceLayout)
        self.drawLayout.add_widget(self.vehicleLayout)
        root.add_widget(layoutBtn)
        print("size of me", root.size)

        Clock.schedule_interval(self.updateListGeoFence, 0.1)
        Clock.schedule_interval(self.updateListVihcle, 0.1)

        return root
        
