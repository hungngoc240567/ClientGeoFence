from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapMarkerPopup
from GraphicClient.ConfigGraphic import *
from GraphicClient.GeoFenceButton import *
from functools import partial
        

class GUILayer(FloatLayout):
    _control = None
    def __init__(self, **kwargs):
        super(GUILayer, self).__init__(**kwargs)
        self.init()

    # hàm khi user bấm vào nút chấp nhận sửa hàng rào
    def onUserAcceptedUpdate(self):
        # 1.1 ẩn button sửa, huỷ sửa và xoá
        self.onVisibleUpdateGeoFence(False)
        # 1.2 gọi mapView thông báo user đồng ý sửa hàng rào
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.onUserAcceptedUpdate()

    def onUserChoseAdd(self):
        self.onVisibleAllAddButton(True)
        return

    def setControlGUI(self, control):
        self._control = control

    def onUserAddGeoFence(self, *largs):
        self._control.onUserStartDrawGeoFence()
        self.onVisibleAllAddButton(False)
        self.onVisibleEnterDenyGeoFence(True)

    def onEnterGeoFence(self, *large):
        self._control.onUserEnterGeoFence()
        self.onVisibleEnterDenyGeoFence(False)
        return

    def onCancelUpdateGeoFence(self):
        self.onVisibleUpdateGeoFence(False)
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.onUserCanelUpdateGeoFence()
        return

    def onUserAddVehicle(self):
        self.onVisibleAllAddButton(False)
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.onUserAddVehcile()
        return

    def onUserDenyGeoFence(self, *large):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.onUserFinishDrawGeoFence()
        self.onVisibleEnterDenyGeoFence(False)
        return

    def onVisibleEnterDenyGeoFence(self, val):
        if not val:
            self.buttonEnterGeoFence.opacity = 0
            self.buttonDeny.opacity = 0
        else:
            self.buttonEnterGeoFence.opacity = 1.0
            self.buttonDeny.opacity = 1.0

    def onVisibleAllAddButton(self, val):
        if not val:
            self.buttonAddGeoFence.opacity = 0
            self.buttonAddVehicle.opacity = 0
        else:
            self.buttonAddGeoFence.opacity = 1.0
            self.buttonAddVehicle.opacity = 1.0

    def onUserDeleteGeoFence(self):
        mapView = GLOBAL_GRAPHIC_VARIABLE['GEO_FENCE_MAP_VIEW']
        mapView.onUserDeleteGeoFence()
        self.onVisibleUpdateGeoFence(False)

    def onVisibleUpdateGeoFence(self, val):
        if not val:
            self.buttonAcceptedUpdate.opacity = 0
            self.buttonDelete.opacity = 0
            self.buttonDenyUpdate.opacity = 0
        else:
            self.buttonAcceptedUpdate.opacity = 1.0
            self.buttonDelete.opacity = 1.0
            self.buttonDenyUpdate.opacity = 1.0

    def createButton(self, contentSize = (100 , 100), anchorPoint = (0.5, 0.5), position = (1700, 2000), imgNoramal = "btn_add.png", imgPress = "btn_add.png", callFunc = None):
        button = GeoFenceButton()
        button.setContentSize(contentSize[0], contentSize[1])
        button.setAnchorPoint(anchorPoint[0], anchorPoint[1])
        button.setPosition(position[0], position[1])
        button.setNormalPressImage(imgNoramal)
        button.setDownPressImage(imgPress)
        button.on_press = partial(callFunc)
        button.opacity = 0
        self.add_widget(button)
        return button

    def do_layout(self, *largs, **kwargs):
        super(GUILayer, self).do_layout(*largs, **kwargs)
        for c in self.children:
            try:
                if hasattr(c, 'update_child_position'):
                    c.update_child_position()
            except:
                print('update_child_position fail')

    def init(self):
        # Khởi tạo button + trên màn hình để thêm hàng rào
        self.buttonAddComon = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(100, 80), imgNoramal="btn_add.png", imgPress="btn_add.png", callFunc=self.onUserChoseAdd)
        # Khởi tạo button thêm sau khi user đã vẽ xong hàng rào
        self.buttonEnterGeoFence = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(1530, 800), imgNoramal="btn_accept.png", imgPress="btn_accept.png", callFunc=self.onEnterGeoFence)
        # Khởi tạo button huỷ thêm
        self.buttonDeny = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(1530, 650), imgNoramal="btn_deny.png", imgPress="btn_deny.png", callFunc=self.onUserDenyGeoFence)
        # Khởi tạo button đồng ý sửa hàng rào
        self.buttonAcceptedUpdate = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(1530, 800), imgNoramal="btn_update.png", imgPress="btn_update.png", callFunc=self.onUserAcceptedUpdate)
        # Khởi tạo button xoá hàng rào
        self.buttonDelete = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(1530, 650), imgNoramal="btn_delete.png", imgPress="btn_delete.png", callFunc=self.onUserDeleteGeoFence)
        # Khởi tạo button huỷ sửa đổi hàng rào
        self.buttonDenyUpdate = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(1530, 500), imgNoramal="btn_deny.png", imgPress="btn_deny.png", callFunc=self.onCancelUpdateGeoFence)
        # Khởi tạo button thêm hàng rào
        self.buttonAddGeoFence = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(100, 230), imgNoramal="btn_add_geo_fence.png", imgPress="btn_add_geo_fence.png", callFunc=self.onUserAddGeoFence)
        # Khởi tạo button thêm phương tiện
        self.buttonAddVehicle = self.createButton((100, 100), anchorPoint=(0.5, 0.5), position=(100, 380), imgNoramal="btn_add_vehicle.png", imgPress="btn_add_vehicle.png", callFunc=self.onUserAddVehicle)
        self.buttonAddComon.opacity = 1
        return
        
        







