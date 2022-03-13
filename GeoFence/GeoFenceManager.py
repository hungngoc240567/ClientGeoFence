from GeoFence.GeoFenceClass import GeoFence
from GeoFence.GeoFenceConfig import *

class GeoFenceManager:
    
    def __init__(self):
        self.listGeoFence = []
        self.initListGeoFence()
    
    def initListGeoFence(self):
        numberGeoFence = geoFenceConfig.getMaxGeoFence()
        for i in range(0, numberGeoFence):
            geoFence = GeoFence()
            self.listGeoFence.append(geoFence)
    

geoFenceMgr = GeoFenceManager()
