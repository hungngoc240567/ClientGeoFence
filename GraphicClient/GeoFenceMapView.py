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
from GeoFence.GeoFenceIAPController import GeoFenceAIPController
from GeoFence.GeoFenceManager import GeoFenceManager
from GraphicClient.ConfigGraphic import *
from GraphicClient.GUILayer import *
from GraphicClient.LayerDrawGeoFence import LayoutDrawGeoFence, LayoutDrawSelectGeoFence
from kivy.core.window import Window
from GeoFence.GeoFenceClass import *
from GraphicClient.LayerDrawVehicle import *
from kivy.clock import Clock

class GeoFenceTouchDraw(FloatLayout):
    _listSaveCoor = []
    _startPointDraw = None
    _control = None
    _isSwallow = False
    _idxPointIsSelect = None
    _startPointAddVehicle = None
    _endPointAddVehicle = None
    _test = None

    def isAddGeoFence(self):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        return mapView.isUserDrawing()

    def isUpdateGeoFence(self):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        return mapView.isUpdateGeoFence()

    def checkIsMove(self, posStart, posEnd):
        deltaX = posEnd[0] - posStart[0]
        deltaY = posEnd[1] - posStart[1]
        return deltaX * deltaX + deltaY * deltaY >= 5 * 5 

    def cleatListSaveCoor(self):
        self._listSaveCoor = []

    def onUserCompleteUpdateGeoFence(self):
        self._idxPointIsSelect = None

    def requestGetCoorByTouch(self, pos):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        return mapView.get_latlon_at(pos[0], pos[1])

    def requestGetXYByCoor(self, coor):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        xy = mapView.get_window_xy_from(lat =coor[0], lon = coor[1], zoom = mapView._zoom)
        return xy

    def on_touch_down(self, touch):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        # case add geo fence
        if self.isAddGeoFence():
            self._startPointDraw = touch.pos
        # case select to update
        elif self.isUpdateGeoFence():
            # case user touch to point in polygon to update point
            self._idxPointIsSelect = mapView.isUserTouchToPoint(touch.pos)
            if self.isUserUpdateGeoFence():
                return True
            return super(GeoFenceTouchDraw, self).on_touch_down(touch)
        elif self.isUserAddVehicle():
            print('co vao day de ve hinh chu nhat ko nhi')
            self._startPointAddVehicle = mapView.get_latlon_at(touch.pos[0], touch.pos[1])
            self._endPointAddVehicle = mapView.get_latlon_at(touch.pos[0], touch.pos[1])
            return True
        # case idle
        else:
            geoFenceController = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_CONTROLLER']
            coor = self.requestGetCoorByTouch(touch.pos)
            ret = geoFenceController.sendGetSelectGeoFence(coor.lat, coor.lon)
            listId = ret['listUid']
            if len(listId) > 0:
                mapView.onUserSelectedGeoFence(listId[len(listId) - 1])
                return True
        return super(GeoFenceTouchDraw, self).on_touch_down(touch)
        

    def on_touch_move(self, touch):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        if self.isUpdateGeoFence():
            if self._idxPointIsSelect != None:
                mapView.updateSelectPoint(self._idxPointIsSelect, touch.pos)
        elif self.isUserAddVehicle():
            self._endPointAddVehicle = mapView.get_latlon_at(touch.pos[0], touch.pos[1])
            mapView.userUpdateRectangleAddGeoFence()
            return True
        return super(GeoFenceTouchDraw, self).on_touch_move(touch)
            
            
    def on_touch_up(self, touch):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        if self.isAddGeoFence():
            if self._startPointDraw != None and not self.checkIsMove(self._startPointDraw, touch.pos):
                coor = self.requestGetCoorByTouch(touch.pos)
                self._listSaveCoor.append(coor)
                self._startPointDraw = None
        if self.isUpdateGeoFence():
            return super(GeoFenceTouchDraw, self).on_touch_up(touch)
        if self.isUserAddVehicle() and self._startPointAddVehicle != None:
            mapView.onUserFinishAddVhicle()
            self._startPointAddVehicle = None
            self._endPointAddVehicle = None
            return super(GeoFenceTouchDraw, self).on_touch_up(touch)
        return super(GeoFenceTouchDraw, self).on_touch_up(touch)

    def getListSaveCoor(self):
        return self._listSaveCoor

    def onUserEnterGeoFence(self):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.do_update(0)

    def isUserUpdateGeoFence(self):
        return self._idxPointIsSelect != None

    def isUserAddVehicle(self):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        return mapView.isUserAddVehicle()

    def getRectangleAddGeoFence(self):
        return (self._startPointAddVehicle, self._endPointAddVehicle)



class GeoFenceMapView(MapView):
    grp = ObjectProperty(None)
    _listDrawGeoFencePoint = []
    _list_save_geo_pos = []
    _startPointDraw = (0, 0)
    _control = None
    _drawObjectLayout = None,
    _drawRectangleAddVehicle = None,
    _selcetGeoFence = None,
    _stateGeoFence = {
        'IDLE': 0,
        'ADD_GEO_FENCE': 1,
        'SELECTED_GEO_FENCE': 2,
        'ADD_VEHICLE': 3,
    }
    _state = None

    def __init__(self, **kwargs):
        super(GeoFenceMapView, self).__init__(**kwargs)
        # Hàng rào được user chọn để update
        self._selcetGeoFence = None

        # Các state của mapView
        self._state = self._stateGeoFence['IDLE']

        # Khởi tạo một layer vẽ các geo fence đang có
        self._drawObjectLayout = LayoutDrawGeoFence(size_hint = (1, 1))
        self.add_widget(self._drawObjectLayout)

        # Khởi tạo một layer để vẽ hàng rào mà user muốn thêm (các hàng rào màu đỏ) 
        self._drawObjectDrawingLayout = FloatLayout()
        self.add_widget(self._drawObjectDrawingLayout)

        # Khởi tạo một layer vẽ hàng rào mà user đang chọn để update (sửa, xoá)
        self._drawSelectGeoFenceLayout = LayoutDrawSelectGeoFence()
        self.add_widget(self._drawSelectGeoFenceLayout)

        # Khởi tạo một layer vẽ hình chữ nhật thêm phương tiện di chuyển
        self._drawRectangleAddVehicle = LayerDrawRectangeToAddVehicle()
        self.add_widget(self._drawRectangleAddVehicle)

        # Khởi tạo một layer vẽ các phương tiện di chuyển
        self._drawVehicleLayout = LayerDrawVehicle()
        self.add_widget(self._drawVehicleLayout)

        # Bởi vì các phương tiện sẽ di chuyển liên tục nên phải
        # update thường xuyên cho layer này cứ 0.3s sẽ update một lần
        Clock.schedule_interval(self._drawVehicleLayout.draw, 0.3)

    # Hàm được gọi khi user đồng ý sửa hàng rào từ layer gui
    def onUserAcceptedUpdate(self):
        # 2.1 gọi class quản lý các hàng rào gửi gói send update lên server
        geoFenceMgr = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER']
        geoFenceMgr.sendUpdateGeoFence(self._selcetGeoFence.getId(), self._selcetGeoFence.getListPoint())
        # 2.2 bỏ hàng rào được chọn đi vì hàng rào này sẽ được update
        self.onUserUnSelectedGeoFence()
        layerDraw = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        # 2.3 gọi layer touch down để xoá index của điểm update đã được lưu từ trước
        layerDraw.onUserCompleteUpdateGeoFence()

    def onUserDeleteGeoFence(self):
        geoFenceMgr = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER']
        layerDraw = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        print("id need delete", self._selcetGeoFence.getId())
        geoFenceMgr.deleteGeoFence(self._selcetGeoFence.getId())
        self.onUserUnSelectedGeoFence()
        layerDraw.onUserCompleteUpdateGeoFence()
        self.do_update(0)

    def setGUIControl(self, control):
        self._control = control

    def onUserStartDrawGeoFence(self):
        self._state = self._stateGeoFence['ADD_GEO_FENCE']

    def onUserFinishDrawGeoFence(self):
        self._state = self._stateGeoFence['IDLE']
        layerTouch = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        layerTouch.cleatListSaveCoor()
        self.do_update(0)

    def onUserCanelUpdateGeoFence(self):
        self._state = self._stateGeoFence['IDLE']
        self._selcetGeoFence  = None
        layerDraw = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        layerDraw.onUserCompleteUpdateGeoFence()
        self.do_update(0)
        return

    def onUserSelectedGeoFence(self, uid):
        self._state = self._stateGeoFence['SELECTED_GEO_FENCE']
        geoFenceMgr = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER']
        guiLayer = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_GUI_LAYER']
        self.id = uid
        self._selcetGeoFence = geoFenceMgr.getGeoFenceById(uid).clone()
        guiLayer.onVisibleUpdateGeoFence(True)
        self.do_update(0)

    def onUserUnSelectedGeoFence(self):
        self._state = self._stateGeoFence['IDLE']
        self._selcetGeoFence = None
        self.do_update(0)

    def onUserAddVehcile(self):
        if self._state != self._stateGeoFence['IDLE']:
            return
        self._state = self._stateGeoFence['ADD_VEHICLE']

    def onUserFinishAddVhicle(self):
        self._state = self._stateGeoFence['IDLE']
        self._drawRectangleAddVehicle.canvas.clear()
        vehicleMgr = GLOBAL_GRAPHIC_VARIABLE['VEHICLE_MANAGER']
        layerTouch = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        ret = layerTouch.getRectangleAddGeoFence()
        vehicleMgr.initVehicleByRange(30, ret[0], ret[1])

    def checkIsMove(self, posStart, posEnd):
        deltaX = posEnd[0] - posStart[0]
        deltaY = posEnd[1] - posStart[1]
        return deltaX * deltaX + deltaY * deltaY >= 5 * 5 

    def isUserDrawing(self):
        return self._state == self._stateGeoFence['ADD_GEO_FENCE']

    def isUpdateGeoFence(self):
        return self._state == self._stateGeoFence['SELECTED_GEO_FENCE']

    def isUserAddVehicle(self):
        return self._state == self._stateGeoFence['ADD_VEHICLE']

    def isUserTouchToPoint(self, touch):
        size = 20
        listCoor = self._selcetGeoFence.getListPoint()
        for i in range(0, len(listCoor)):
            pos = self.get_window_xy_from(lat = listCoor[i].getX(), lon = listCoor[i].getY(), zoom = self._zoom)
            if pos[0] - size / 2 <= touch[0] and touch[0] + size / 2 >= touch[0] and pos[1] - size / 2 <= touch[1] and pos[1] + size / 2 >= touch[1]:
                return i
        return None

    def updateSelectPoint(self, idx, touch):
        geoFence = self._selcetGeoFence
        listCoor = geoFence.getListPoint()
        if len(listCoor) <= 0:
            return
        pos = self.get_latlon_at(touch[0], touch[1])
        listCoor[idx].setX(pos.lat)
        listCoor[idx].setY(pos.lon)
        self.do_update(0)
    
    def userUpdateRectangleAddGeoFence(self):
        rectangleDrawVehcile = self.getRectangleAddGeoFence()
        self._drawRectangleAddVehicle.draw(rectangleDrawVehcile[0], rectangleDrawVehcile[1])

    def do_update(self, dt):  # this over-rides the do_update() method of MapView
        super(GeoFenceMapView, self).do_update(dt)
        self.draw_lines()
        self._drawVehicleLayout.draw(0)
        
    def getLineDrawingAddGeoFence(self):
        points = []
        layerTouch = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        listDrawGeoFencePoint = layerTouch.getListSaveCoor()
        for coor in listDrawGeoFencePoint:
            point = self.get_window_xy_from(lat = coor.lat, lon = coor.lon, zoom = self._zoom)
            points.append([point[0], point[1]])
        lines = Line(points = points)
        return lines

    def getListDrawingGeoFence(self, listGeoFence):
        listLine = []
        for id in listGeoFence:
            geoFence = listGeoFence[id]
            listPoint = geoFence.getListPoint()
            line = []
            for point in listPoint:
                xy = self.get_window_xy_from(lat = point.getX(), lon = point.getY(), zoom = self._zoom)
                line.append([xy[0], xy[1]])
            listLine.append(Line(points =line))
        return listLine

    def draw_lines(self):
        geoFenceMgr = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MANAGER']
        lines = self.getLineDrawingAddGeoFence()
        self._drawObjectDrawingLayout.canvas.clear()
        with self._drawObjectDrawingLayout.canvas:
                #  create the group and add the lines
                Color(1,0,0,1)  # line color
                Line(points = lines.points)
        id = None
        if self._selcetGeoFence != None:
            id = self._selcetGeoFence.getId()
        self._drawObjectLayout.draw(geoFenceMgr.getListGeoFence(), id)
        self._drawSelectGeoFenceLayout.draw(self._selcetGeoFence)

    def getRectangleAddGeoFence(self):
        layerTouch = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        ret = layerTouch.getRectangleAddGeoFence()
        if ret[0] == None:
            return (None, None)
        return (self.get_window_xy_from(lat=ret[0].lat, lon=ret[0].lon, zoom = self._zoom), self.get_window_xy_from(lat=ret[1].lat, lon=ret[1].lon, zoom = self._zoom))
    
    def onUserEnterGeoFence(self):
        layerTouch = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_TOUCH_DRAW']
        layerTouch.onUserEnterGeoFence()
        listCoor = layerTouch.getListSaveCoor()
        listPoint = []
        for coor in listCoor:
            listPoint.append({'x': coor.lat, 'y': coor.lon})
        layerTouch.cleatListSaveCoor()
        self._state = self._stateGeoFence['IDLE']
        return listPoint
