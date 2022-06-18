from turtle import pos
from kivy.uix.floatlayout import FloatLayout
from numpy import size
from GraphicClient.ConfigGraphic import *
from kivy.graphics import Color, Rectangle, Point, Line
from kivy.core.window import Window

class LayerDrawVehicle(FloatLayout):
    def draw(self, dt):
        self.canvas.clear()
        with self.canvas:
            # Lấy các biến global
            vehicleMgr = GLOBAL_GRAPHIC_VARIABLE['VEHICLE_MANAGER']
            geoFenceMgr = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER']
            mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
            # Lấy list phương tiện
            listVehicle = vehicleMgr.getListVehicle()
            # Lấy toạ độ thực từ điểm (0, 0) đến điểm (width, height) của màn hình
            coorOrigin = mapView.get_latlon_at(0, 0)
            coorScreen = mapView.get_latlon_at(Window.size[0], Window.size[1])
            for vehicle in listVehicle:
                coor = vehicle.getPoint()
                # Tính toán toà độ thực của phương tiện sang toà độ màn hình
                point = mapView.get_window_xy_from(lat = coor.getX(), lon = coor.getY(), zoom = mapView._zoom)
                # Lấy list id các geo fence mà phương tiện nằm ở trong
                listGeoFenceIn = vehicle.getListIdGeoFenceIn()
                # Kiểm tra toà độ thực của phương tiện có nằm trong phần toà độ thực của màn hình
                if coor.getX() > coorOrigin.lat and coor.getX() < coorScreen.lat and coor.getY() > coorOrigin.lon and coor.getY() < coorScreen.lon:
                    Color(0.1, 1, 1, mode = 'hsv')
                    Rectangle(pos = (point[0], point[1]), size = (10, 10))
                    for j in range(0, len(listGeoFenceIn)):
                        id = listGeoFenceIn[j]
                        # Lấy màu của hàng rào mà phương tiện nằm bên trong
                        color = geoFenceMgr.getGeoFenceColorById(id)
                        if color == None:
                            continue
                        Color(color, 1, 1, mode = 'hsv')
                        # Vẽ các hàng màu đó kế bên màu của phương tiện để biểu thị phương tiện ở trong hàng rào
                        Rectangle(pos = (point[0] + (j + 1) * 10, point[1]), size = (10, 10))

class LayerDrawRectangeToAddVehicle(FloatLayout):
    def draw(self, posStart, posEnd):
        # Xoá hình chữ nhật thêm xe cũ đi
        self.canvas.clear()
        # check xem nếu ko có start point thì không cần vẽ
        if posStart == None:
            return
        with self.canvas:
            # Tính chiều dài, chiều rộng của hình chữ nhật
            sizeWidth = posEnd[0] - posStart[0]
            sizeHeight = posEnd[1] - posStart[1]
            # set màu vẽ cho hình chữ nhật
            Color(1, 0.5, 0.8, 1)
            # Vẽ hình chữ nhật bằng 4 đoạn thẳng
            points = [posStart, (posStart[0], posStart[1] + sizeHeight), posEnd, (posStart[0] + sizeWidth, posStart[1]), posStart]
            Line(points = points, width = 2)
                        
                    
                    






    