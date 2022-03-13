import requests
from Vehicle.VehicleManager import *
from GeoFence.GeoFenceManager import *

def __main__():
    # khởi tạo list geofence
    geoFenceMgr.initListGeoFence()

    # Khởi tạo list phương tiện
    vehicleMgr.initVehicle()
    # Cho list phương tiện chạy lung tung
    # để server check xem phương tiện có ở trong
    # geofence nào không
    vehicleMgr.letAllVehicleMove()

__main__()