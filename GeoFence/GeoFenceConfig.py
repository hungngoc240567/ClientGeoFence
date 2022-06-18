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

        self.minRangeInitX = config["min_range_init_X"]
        self.maxRangeInitX = config["max_range_init_X"]
        self.minRangeInitY = config["min_range_init_Y"]
        self.maxRangeInitY = config["max_range_init_Y"]
        self.minLenInitX = config["min_len_range_init_X"]
        self.maxLenInitX = config["max_len_range_init_X"]
        self.minLenInitY = config["min_len_range_init_Y"]
        self.maxLenInitY = config["max_len_range_init_Y"]
         

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

    def getMinRangeInitX(self):
        return self.minRangeInitX

    def getMaxRangeInitX(self):
        return self.maxRangeInitX
    
    def getMinRangeInitY(self):
        return self.minRangeInitY

    def getMaxRangeInitY(self):
        return self.maxRangeInitY
    
    def getMinLenInitX(self):
        return self.minLenInitX

    def getMaxLenInitX(self):
        return self.maxLenInitX

    def getMinLenInitY(self):
        return self.minLenInitY

    def getMaxLenInitY(self):
        return self.maxLenInitY



    def print(self):
        print("router: " + self.getRouterPath() + "\n"
            + "max time random: " + str(self.getMaxGeoFence()) + "\n"
            + "min time random: " + str(self.getMaxPointInGeoFence()) + "\n"
            + "max range random: " + str(self.getMinRangeRandom()) + "\n"
            + "min range random: " + str(self.getMaxRangeRandom()) +"\n"
            + "min range init X: " + str(self.getMinRangeInitX()) +"\n"
            + "max range init X: " + str(self.getMaxRangeInitX()) +"\n"
            + "min range init Y: " + str(self.getMinRangeInitY()) +"\n"
            + "max range initY: " + str(self.getMaxRangeInitY()) +"\n"
            + "min len init X: " + str(self.getMinLenInitX()) +"\n"
            + "max len init X: " + str(self.getMaxLenInitX()) +"\n"
            + "min len init Y: " + str(self.getMinLenInitY()) +"\n"
            + "max len init Y: " + str(self.getMaxLenInitY()) +"\n")

geoFenceConfig = LoadConfigGeoFence()
geoFenceConfig.print()
print("On finish load config geofence!\n")