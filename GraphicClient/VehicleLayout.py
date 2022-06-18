from statistics import mode
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

class VehicleLayout(FloatLayout):
    def drawListVehicle(self, listVehicle, geoFenceMgr):
        self.canvas.clear()
        with self.canvas:
            listGeoFence = geoFenceMgr.getListGeoFence()
            for i in range(len(listVehicle)):
                vehicle = listVehicle[i]
                point = (vehicle.getPoint().getX(), vehicle.getPoint().getY())
                listIdGeoFenceIn = vehicle.getListIdGeoFenceIn()
                Color(0.0, 1, 1, mode = 'hsv')
                Rectangle(pos = (point[0], point[1]), size = (10, 10))
                for j in range(len(listIdGeoFenceIn)):
                    # check truoc xem id co ton tai trong list geo fence khong
                    # tranh truong hop id nay chua ve kip khi goi bat dong bo
                    if(listIdGeoFenceIn[j] in listGeoFence):
                        geoFenceIn = listGeoFence[listIdGeoFenceIn[j]]
                        color = geoFenceIn.getColorHSV()
                        Color(color, 1, 1, mode = 'hsv')
                        Rectangle(pos = (point[0] + (j + 1) * 10, point[1]), size = (10, 10))