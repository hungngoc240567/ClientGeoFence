import imp
import math
from re import X
from urllib import response
from numpy import MachAr
import requests
from GeoFence.GeoFenceConfig import *

class GeoFenceAIPController:
    def __init__(self):
        self.router = geoFenceConfig.getRouterPath()
        
    
    def sendInitGeoFence(self, listInitPoint):
        json = {"points": listInitPoint}
        response = requests.post(self.router, json = json)
        return response.json()
        
        
        
geoFenceController = GeoFenceAIPController()