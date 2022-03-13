import imp
import sys
# Thay đường dẫn của mọi người đến thư mục này hen
sys.path.append('/Users/lap13994/Documents/FinalGeoFenceProject/ClientGeoFence/')
from SupportClass.Point import Point
from GeoFence.GeoFenceConfig import *
from GeoFence.GeoFenceIAPController import *

import random
class GeoFence:
    def __init__(self):
        self.listPoint = []
        self.id = None
        listInitPoint = self.genarateRandomListPoint()
        # send lên server thông tin các điểm được random
        # trả về id và tập điểm bao lồi cho client
        ret = geoFenceController.sendInitGeoFence(listInitPoint)
        self.id = ret["id"]
        listConvexPoint = ret["listConvexPoint"]
        for i in range(0, len(listConvexPoint)):
            self.listPoint.append(Point(listConvexPoint[i]["x"], listConvexPoint[i]["y"]))



    def genarateRandomListPoint(self):
        minRange = geoFenceConfig.getMinRangeRandom()
        maxRange = geoFenceConfig.getMaxRangeRandom()
        maxPointInGeoFence = geoFenceConfig.getMaxPointInGeoFence()
        listInitPoint = []
        for i in range(0, maxPointInGeoFence):
            randX = random.uniform(0, maxRange) - minRange
            randY = random.uniform(0, maxRange) - minRange
            listInitPoint.append({"x": randX, "y": randY})
        return listInitPoint


geoFence = GeoFence()