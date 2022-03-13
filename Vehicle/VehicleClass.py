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
    def __init__(self):
        super(Vehicle, self) .__init__()
        self.id = None
        self.curPoint = self.generateInitRandomPosition()
        # send lên server thông tin khởi tạo và server sẽ
        # trả về id của phương tiện
        self.id = vehicleController.sendInitVehicle(self)
        self.listIdGeoGence = []

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
        randX = random.uniform(0, vehicleConfig.getMaxRangeRandom()) - vehicleConfig.getMinRangeRandom()
        randY = random.uniform(0, vehicleConfig.getMaxRangeRandom()) - vehicleConfig.getMinRangeRandom()
        newPoint.x = point.x + randX * time
        newPoint.y = point.y + randY * time
        return newPoint

    def generateInitRandomPosition(self):
        randX = random.uniform(0, vehicleConfig.getMaxInitPosition()) - vehicleConfig.getMinInitPosition()
        randY = random.uniform(0, vehicleConfig.getMaxInitPosition()) - vehicleConfig.getMinInitPosition()
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

    