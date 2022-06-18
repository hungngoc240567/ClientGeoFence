import imp
import sys

from scipy import rand
# Thay đường dẫn của mọi người đến thư mục này hen
sys.path.append('/Users/lap13994/Documents/FinalGeoFenceProject/ClientGeoFence/')
from SupportClass.Point import Point
from GeoFence.GeoFenceConfig import *
from GeoFence.GeoFenceIAPController import *
from SupportClass.GeneratePoligon import *

import random
class GeoFence:
    def __init__(self, listServerPoint = [], id = None):
        self.listPoint = []
        self.id = None
        # mau duoi dang hsv cua geo fence nay khi
        # dc draw len man hinh
        self.color = None
        # send lên server thông tin các điểm được random
        # trả về id và tập điểm bao lồi cho client
        self.id = id
        for i in range(0, len(listServerPoint)):
            self.listPoint.append(Point(listServerPoint[i]["x"], listServerPoint[i]["y"]))
        self.saveMinMaxXY()

    def clone(self):
        clone = GeoFence()
        clone.listPoint = []
        for point in self.listPoint:
            clone.listPoint.append(Point(point.getX(), point.getY()))
        clone.id = self.id
        clone.saveMinMaxXY()
        return clone

    def saveMinMaxXY(self):
        if len(self.listPoint) < 1:
            return
        self.maxX = self.listPoint[0].getX()
        self.minX = self.listPoint[0].getX()
        self.maxY = self.listPoint[0].getY()
        self.minY = self.listPoint[0].getY()
        for i in range(1, len(self.listPoint)):
            point = self.listPoint[i]
            if point.getX() > self.maxX:
                self.maxX = point.getX()
            if point.getX() < self.minX:
                self.minX = point.getX()
            if point.getY() > self.maxY:
                self.maxY = point.getY()
            if point.getY() < self.minY:
                self.minY = point.getY()


    def genarateRandomListPoint(self):
        minRangeInitX = geoFenceConfig.getMinRangeInitX()
        maxRangeInitX = geoFenceConfig.getMaxRangeInitX()
        initX = random.uniform(0, maxRangeInitX) + minRangeInitX

        minRangeInitY = geoFenceConfig.getMinRangeInitY()
        maxRangeInitY = geoFenceConfig.getMaxRangeInitY()
        initY = random.uniform(0, maxRangeInitY) + minRangeInitY

        minLenInitX = geoFenceConfig.getMinLenInitX()
        maxLenInitX = geoFenceConfig.getMaxLenInitX()
        initLenX = random.uniform(0, maxLenInitX) + minLenInitX
        if initLenX + initX > 1600:
            initLenX = 1600 - initX

        minLenInitY = geoFenceConfig.getMinLenInitY()
        maxLenInitY = geoFenceConfig.getMaxLenInitY()
        initLenY = random.uniform(0, maxLenInitY) + minLenInitY
        if initLenY + initX > 1150:
            initLenY = 1150 - initY
        
        listInitPoint = []
        listPointGenerate = generatePolygonMgr.generate_polygon(Point(initX, initY), initLenX, 0.2, 0.3, geoFenceConfig.getMaxPointInGeoFence())
        for i in range(len(listPointGenerate)):
            point = listPointGenerate[i]
            listInitPoint.append({"x":point.getX(), "y": point.getY()})
        
        return listInitPoint

    def getListConvex(self):
        return self.listPoint

    def getListPoint(self):
        return self.listPoint

    def getListInitPoint(self):
        return self.listInitPoint

    def setColorHSV(self, val):
        self.color = val
    
    def getColorHSV(self):
        return self.color

    def getId(self):
        return self.id

    def listInitPointTest(self):
        listInitPoint = []
        listInitPoint.append({"x":642.6784912638032, "y":413.9035670973724})
        listInitPoint.append({"x":724.3094736330808, "y":710.034347252661})
        listInitPoint.append({"x":261.71870271448586, "y":994.2886067224424})
        listInitPoint.append({"x":945.0564148495438, "y":482.0726346083537})
        listInitPoint.append({"x":261.7316097511801, "y":521.0517128458358})
        listInitPoint.append({"x":908.8710430961203, "y":937.7696475071396})
        listInitPoint.append({"x":965.4399436309191, "y":491.90959400288074})
        listInitPoint.append({"x":937.3285869852559, "y":691.977006260246})
        listInitPoint.append({"x":469.831950816467, "y":243.00393863696542})
        listInitPoint.append({"x":200.8089925648992, "y":800.7216569388066})
        listInitPoint.append({"x":509.43282449061644, "y":302.0036707446118})
        listInitPoint.append({"x":828.7622078097255, "y":267.1665500201618})
        listInitPoint.append({"x":549.7029871642833, "y":552.2113321346137})
        listInitPoint.append({"x":779.0724899810396, "y":589.4613717504667})
        listInitPoint.append({"x":846.2592986746555, "y":531.4633732315544})
        listInitPoint.append({"x":871.1517422779725, "y":729.9587728817608})
        listInitPoint.append({"x":795.6562187503528, "y":634.8798141676721})
        listInitPoint.append({"x":539.9447889650025, "y":720.1742489865188})
        listInitPoint.append({"x":435.6808789978536, "y":553.4860101622742})
        listInitPoint.append({"x":349.23406210130395, "y":733.0329027584945})
        listInitPoint.append({"x":717.1379730617676, "y":440.273536930379})
        listInitPoint.append({"x":728.1190282835994, "y":766.9610353373512})
        listInitPoint.append({"x":969.3597996784363, "y":731.8885885329967})
        listInitPoint.append({"x":922.3670753368629, "y":834.9188148669268})
        listInitPoint.append({"x":948.6960230421887, "y":249.72710627042335})
        listInitPoint.append({"x":417.7977165432585, "y":436.81224104205774})
        listInitPoint.append({"x":580.6587204920993, "y":875.2426803584035})
        listInitPoint.append({"x":350.3487878519457, "y":359.89801385738537})
        listInitPoint.append({"x":872.6255983299119, "y":795.0265949330508})
        listInitPoint.append({"x":497.862804450945, "y":445.2962168176779})
        return listInitPoint
        
    def getListEdge(self):
        return self.listEdge

    def getOriginPoint(self):
        return self.originPoint

    def print(self):
        print(self.id)
        for i in range (0, len(self.listPoint)):
            self.listPoint[i].print()

    def isInArea(self, lowX, highX, lowY, highY):
        for point in self.listPoint:
            if point.getX() >= lowX and point.getX() <= highX and point.getY() >= lowY and point.getY() <= highY:
                return True
        return False

    def getBondingArea(self):
        return abs(self.maxX - self.minX) * abs(self.maxY - self.minY)



# geoFence = GeoFence()