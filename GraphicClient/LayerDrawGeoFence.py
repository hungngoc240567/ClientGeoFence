import random
from kivy.uix.floatlayout import FloatLayout
from GraphicClient.ConfigGraphic import *
from kivy.graphics import Color, Rectangle, Point, Line
from kivy.core.window import Window

class LayoutDrawGeoFence(FloatLayout):
    def draw(self, listGeoFence, idGeoFenceSelect):
        self.canvas.clear()
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        # Lấy toạ độ thực từ điểm (0, 0) đến điểm (width, height) của màn hình
        coorOrigin = mapView.get_latlon_at(0, 0)
        coorScreen = mapView.get_latlon_at(Window.size[0], Window.size[1])
        # Tính diện tích phần màn hình theo toạ độ thực
        areaScreen = abs(coorScreen.lon - coorOrigin.lon) * abs(coorScreen.lat - coorOrigin.lat)
        with self.canvas:
            for id in listGeoFence:
                # Trường hợp hàng rào có là hàng rào đang đang user chọn thì không vẽ
                # mà sẽ để cho layer select geo fence vẽ hàng rào này
                if id == idGeoFenceSelect:
                    continue
                geoFence = listGeoFence[id]
                # Tính diện tích của hàng rào dựa trên toạ độ thực (lot, lon)
                area = geoFence.getBondingArea()
                # Lấy các điểm trong hàng rào để vẽ
                listGeoFencePoint = geoFence.getListPoint()
                points = []
                # Điều kiện để vẽ hàng rào là diện tích của hàng rào phải lớn hơn hoặc bằng 1/200 diện tích của màn hình hiện tại tính 
                # theo toạ độ thực (lat, lon) và tồn tại ít nhất 1 điểm của hàng rào năm trong màn hình mới được hiển thị
                if areaScreen <= area * 200 and geoFence.isInArea(coorOrigin.lat, coorScreen.lat, coorOrigin.lon, coorScreen.lon):
                    # Lưu lại các toạ độ điểm của hàng rào
                    for coor in listGeoFencePoint:
                        # Đổi các toạ độ điểm này từ toạ độ thực (lat, lon) thành toạ độ màn hình để vẽ
                        point = mapView.get_window_xy_from(lat = coor.getX(), lon = coor.getY(), zoom = mapView._zoom)
                        points.append([point[0], point[1]])
                    # Lưu thêm điểm đầu của hàng rào vào list point để hàng rào được khép kín
                    coor = listGeoFencePoint[0]
                    point = mapView.get_window_xy_from(lat = coor.getX(), lon = coor.getY(), zoom = mapView._zoom)
                    points.append([point[0], point[1]])
                    # Lấy màu của hàng rào để vẽ lên màn hình
                    Color(geoFence.getColorHSV(), 1, 1, mode = 'hsv')
                    # Nếu hàng rào có diện tích càng lớn thì đường vẽ càng lớn max của đường vẽ là 8px
                    maxWidth = 8
                    deltaArea = area / areaScreen
                    width = maxWidth * deltaArea
                    if width < 1:
                        width = 1
                    if width > 8:
                        width = 8
                    # Vẽ hàng rào đã được thoả điều kiện lên màn hình
                    Line(points = points, width = width)

class LayoutDrawSelectGeoFence(FloatLayout):
    def draw(self, geoFence):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        points = []
        self.canvas.clear()
        # Nếu không có hàng rào nào đang được chọn thì không cần vẽ
        if geoFence == None:
            return
        with self.canvas:
            Color(1, 0.5, 0.8, 1)
            listPoint = geoFence.getListPoint()
            # Lấy các điểm trong hàng rào để vẽ
            for coor in listPoint:
                # Đổi các toạ độ điểm này từ toạ độ thực (lat, lon) thành toạ độ màn hình để vẽ
                point = mapView.get_window_xy_from(lat = coor.getX(), lon = coor.getY(), zoom = mapView._zoom)
                size = 20
                # Vẽ các đầu mút (đỉnh của hàng rào) là những hình vuông
                Rectangle(pos = (point[0] - size / 2, point[1] - size / 2), size = (size, size))
                points.append([point[0], point[1]])
            coor = listPoint[0]
            # Lưu thêm điểm đầu của hàng rào vào list point để hàng rào được khép kín
            point = mapView.get_window_xy_from(lat = coor.getX(), lon = coor.getY(), zoom = mapView._zoom)
            points.append([point[0], point[1]])
            # Vẽ hàng rào mà user đang chọn lên màn hình
            Line(points = points, width = 2)
            
        
                

            
        
