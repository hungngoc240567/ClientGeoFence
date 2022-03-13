import imp
import json
import os

csfp = os.path.dirname(os.path.realpath(__file__))
class LoadConfigGeoFence:
    def __init__(self):
        json_file = os.path.join(csfp, "Config.json")
        with open(json_file) as jsonConfig:
            config = json.load(jsonConfig)
        self.router = config["router_path"]
        self.maxGeoFence = config["max_geo_fence"]
        self.maxPointInGeoFence = config["max_point_in_geo_fence"]
        self.maxRangeRandomInit = config["max_range_random_init"]
        self.minRangeRandomInit = config["min_range_random_init"]

    def getMaxGeoFence(self):
        return self.maxGeoFence

    def getMaxPointInGeoFence(self):
        return self.maxPointInGeoFence

    def getMinRangeRandom(self):
        return self.minRangeRandomInit
    
    def getMaxRangeRandom(self):
        return self.maxRangeRandomInit

    def getRouterPath(self):
        return self.router

    def print(self):
        print("router: " + self.getRouterPath() + "\n"
            + "max time random: " + str(self.getMaxGeoFence()) + "\n"
            + "min time random: " + str(self.getMaxPointInGeoFence()) + "\n"
            + "max range random: " + str(self.getMinRangeRandom()) + "\n"
            + "min range random: " + str(self.getMaxRangeRandom()) +"\n")

geoFenceConfig = LoadConfigGeoFence()
geoFenceConfig.print()
print("On finish load config geofence!\n")