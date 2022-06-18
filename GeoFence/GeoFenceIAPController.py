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
        ret = response.json()
        return response.json()

    def sendGetAllGeoFence(self):
        response = requests.get(self.router)
        return response.json()

    def sendGetSelectGeoFence(self, x, y):
        json = {'point': {'x':x, 'y': y}}
        response = requests.post(self.router + "/selectGeoFence", json = json)
        return response.json()

    def sendUpdateGeoFence(self, id, listPoint):
        json = {"id":id, "listPoint": listPoint}
        response = requests.put(self.router, json = json)
        return response.json()

    def sendDeleteGeoFence(self, id):
        json = {"id":id}
        response = requests.delete(self.router+"/"+id, json = json)
        return response.json()
        
        
        
geoFenceController = GeoFenceAIPController()