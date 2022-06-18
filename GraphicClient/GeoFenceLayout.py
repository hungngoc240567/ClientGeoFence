import math
import random
from statistics import mode
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Line

class GeoFenceLayout(FloatLayout):
    def setInit(self):
        self.isFirstDraw = True
    
    def drawListGeoFence(self, geoFenceMgr):
        listGeoFence = geoFenceMgr.getListGeoFence()
        
        with self.canvas:
            for geoFence in listGeoFence.values():
                points = []
                listPoint = geoFence.getListConvex()
                color = geoFence.getColorHSV()
                for i in range(len(listPoint)):
                    points.append(listPoint[i].getX())
                    points.append(listPoint[i].getY())
                points.append(listPoint[0].getX())
                points.append(listPoint[0].getY())
                Color(color, 1, 1, mode = 'hsv')
                Line(points = points)
                    





            
            
