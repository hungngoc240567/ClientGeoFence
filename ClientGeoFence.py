import requests
from Vehicle.VehicleManager import *
from GeoFence.GeoFenceManager import *
from GraphicClient.AppClient import *

def __main__():
    # khởi tạo list geofence
    geoFenceMgr = GeoFenceManager()

    # Khởi tạo list phương tiện
    vehicleMgr = VehicleManager()
    
    # Khởi tạo phần đồ hoạ client
    geoFenceClientApp = AppGeoFenceClient()
    geoFenceClientApp.setInfoMgr(geoFenceMgr, vehicleMgr)
    geoFenceClientApp.run()

__main__()