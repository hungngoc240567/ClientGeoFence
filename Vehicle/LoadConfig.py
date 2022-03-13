import imp
import json
import os

csfp = os.path.dirname(os.path.realpath(__file__))
class LoadConfig:
    def __init__(self):
        json_file = os.path.join(csfp, "Config.json")
        with open(json_file) as jsonConfig:
            config = json.load(jsonConfig)
        self.router = config["router_path"]
        self.updatePositionPath = config["update_position_path"]
        self.maxRangeRandom = config["max_range_random"]
        self.minRangeRandom = config["min_range_random"]
        self.maxTimeRandom = config["max_time_random"]
        self.minTimeRandom = config["min_time_random"]
        self.maxInitPosition = config["max_init_position"]
        self.minInitPosition = config["min_init_position"]
        self.numberVehicle = config["number_vehicle"]

    def getMinTimeRandom(self):
        return self.minTimeRandom

    def getMaxTimeRandom(self):
        return self.maxTimeRandom

    def getMinRangeRandom(self):
        return self.minRangeRandom
    
    def getMaxRangeRandom(self):
        return self.maxRangeRandom

    def getMaxInitPosition(self):
        return self.maxInitPosition
    
    def getMinInitPosition(self):
        return self.minInitPosition
    
    def getRouterPath(self):
        return self.router

    def getNumberVehicle(self):
        return self.numberVehicle

    def getUpdatePositionRouter(self):
        return self.getRouterPath() + self.updatePositionPath

    def print(self):
        print("router: " + self.getRouterPath() + "\n"
            + "max time random: " + str(self.getMaxTimeRandom()) + "\n"
            + "min time random: " + str(self.getMinTimeRandom()) + "\n"
            + "max range random: " + str(self.getMaxRangeRandom()) + "\n"
            + "min range random: " + str(self.getMinRangeRandom()) +"\n"
            + "update_position_router: " + str(self.getUpdatePositionRouter()) + "\n"
            + "max_init_position: " + str(self.getMaxInitPosition()) + "\n"
            + "min_init_position: " + str(self.getMinInitPosition()) + "\n"
            + "number_vehicle: " + str(self.getNumberVehicle()) + "\n")

vehicleConfig = LoadConfig()
vehicleConfig.print()
print("On finish load config vehicle!\n")