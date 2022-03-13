import imp
from re import X
from urllib import response
import requests
from Vehicle.LoadConfig import *

class VehicleAIPController:
    def __init__(self):
        self.router = vehicleConfig.getRouterPath()
        self.routerUpdatePosition = vehicleConfig.getUpdatePositionRouter()
    
    def sendInitVehicle(self, vehicle):
        json = {"type": "", "point" : {"x": 0, "y": 0}}
        json["point"]["x"] = vehicle.getPoint().getX()
        json["point"]["y"] = vehicle.getPoint().getY()
        response = requests.post(self.router, json = json)
        return response.json()

    def sendUpdatePositionVehicle(self, vehicle):
        jsonBody = {"id": vehicle.getId(), "point": {"x": vehicle.getPoint().getX(), "y": vehicle.getPoint().getY()}}
        response = requests.put(self.routerUpdatePosition, json = jsonBody)
        return response.json()
        
vehicleController = VehicleAIPController()