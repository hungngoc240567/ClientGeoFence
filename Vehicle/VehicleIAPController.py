import imp
from re import X
from urllib import response
import requests
from Vehicle.LoadConfig import *

class VehicleAIPController:
    def __init__(self):
        self.router = vehicleConfig.getRouterPath()
        self.routerUpdatePosition = vehicleConfig.getUpdatePositionRouter()
    
    def sendInitVehicle(self, pos, vx, vy):
        json = {"type": "", "point" : {"x": pos.getX(), "y": pos.getY()}, "vx": vx, "vy": vy}
        response = requests.post(self.router, json = json)
        return response.json()

    def sendUpdatePositionVehicle(self, vehicle):
        jsonBody = {"id": vehicle.getId(), "point": {"x": vehicle.getPoint().getX(), "y": vehicle.getPoint().getY()}}
        response = requests.put(self.routerUpdatePosition, json = jsonBody)
        return response.json()
        
    def sendGetListVehicle(self):
        response = requests.get(self.router)
        return response.json()
vehicleController = VehicleAIPController()