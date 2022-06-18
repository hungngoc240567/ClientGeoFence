import imp
from time import sleep
# from LoadConfig import *
import sys
# Thay đường dẫn của mọi người đến thư mục này hen
sys.path.append('/Users/lap13994/Documents/FinalGeoFenceProject/ClientGeoFence/')
from SupportClass.Point import Point
from Vehicle.LoadConfig import *
from Vehicle.VehicleIAPController import *
import random
from threading import Thread

class Vehicle(Thread):
    def __init__(self, id =None, pos=Point(0, 0), listIdGeoFenceIn = [],vx = 0, vy = 0):
        super(Vehicle, self) .__init__()
        self.id = id
        self.curPoint = pos
        self.vx = vx
        self.vy = vy
        self.listIdGeoGence = listIdGeoFenceIn

    def getPoint(self):
        return self.curPoint

    def setPoint(self, point):
        self.curPoint = point

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getListIdGeoFenceIn(self):
        return self.listIdGeoGence

    def setListIdGeoFenceIn(self, listId):
        self.listIdGeoGence = listId

    def onMoveNext(self):
        timeMove = random.uniform(vehicleConfig.getMinRangeRandom(), vehicleConfig.getMaxTimeRandom())
        self.generateNextPoint(timeMove)
        return timeMove

    def generateNextPoint(self, time):
        point = self.getPoint()
        newPoint = Point(0, 0)
        randX = self.vx
        if random.uniform(0, 1) >= 0.5:
            randX *= -1
        randY = self.vy
        if random.uniform(0, 1) >= 0.5:
            randY*=-1
        newPoint.x = point.x + randX * time
        newPoint.y = point.y + randY * time
        return newPoint

    def generateInitRandomPosition(self):
        randX = random.uniform(0, vehicleConfig.getMaxInitPosition()) + vehicleConfig.getMinInitPosition()
        randY = random.uniform(0, vehicleConfig.getMaxInitPosition()) + vehicleConfig.getMinInitPosition()
        return Point(randX, randY)

    def onDrawOnScreen(self):
        # TODO: hàm này sẽ dùng để vẽ UI trên màn hình
        # self.print()
        return

    def run(self):
        while(True):
            time = self.onMoveNext()
            point = self.generateNextPoint(time)
            sleep(time)
            # TODO: send packet update position to server
            listId = vehicleController.sendUpdatePositionVehicle(self)
            self.setListIdGeoFenceIn(listId)
            self.setPoint(point)
            self.onDrawOnScreen()

    def print(self):
        print(self.id)
        print(self.curPoint)
        print(self.listIdGeoGence)

    