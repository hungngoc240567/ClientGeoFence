from tracemalloc import start
from Vehicle.LoadConfig import *
from Vehicle.VehicleClass import *

class VehicleManager:
    
    def __init__(self):
        self.listVehicle = []
        self.onSendGetAllVehicle()

    def onSendGetAllVehicle(self):
        ret = vehicleController.sendGetListVehicle()
        for infoVehicle in ret:
            vehicle = Vehicle(id= infoVehicle['id'], pos = Point(infoVehicle['curPoint']['x'], infoVehicle['curPoint']['y']), vx= infoVehicle['vx'], vy = infoVehicle['vy'])
            self.listVehicle.append(vehicle)
            vehicle.start()



    def addVehicle(self, num):
        for i in range(num):
            vehicle = Vehicle()
            self.listVehicle.append(vehicle)
            vehicle.start()
    
    def getListVehicle(self):
        return self.listVehicle

    def initVehicleByRange(self, num, startPos, endPos):
        vx = abs(endPos.lat - startPos.lat) / 500
        vy = abs(endPos.lon - startPos.lon) / 500
        print(vx, vy)
        for i in range(0, num):
            pos = Point(random.uniform(startPos.lat, endPos.lat), random.uniform(startPos.lon, endPos.lon))
            ret = vehicleController.sendInitVehicle(pos, vx, vy)
            print("what is ret", ret)
            vehicle = Vehicle(id=ret, pos = pos, listIdGeoFenceIn=[], vx=vx, vy=vy)
            self.listVehicle.append(vehicle)
            vehicle.start()
        

