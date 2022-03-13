from Vehicle.LoadConfig import *
from Vehicle.VehicleClass import *

class VehicleManager:
    
    def __init__(self):
        self.listVehicle = []
        self.initVehicle()
    
    def initVehicle(self):
        numberVehicle = vehicleConfig.getNumberVehicle()
        for i in range(0, numberVehicle):
            vehicle = Vehicle()
            self.listVehicle.append(vehicle)

    def letAllVehicleMove(self):
        for i in range(0, len(self.listVehicle)):
            vehicle = self.listVehicle[i]
            vehicle.start()
    

vehicleMgr = VehicleManager()
