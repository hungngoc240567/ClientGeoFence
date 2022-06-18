from warnings import catch_warnings
from GeoFence.GeoFenceClass import GeoFence
from GeoFence.GeoFenceConfig import *
from GeoFence.GeoFenceIAPController import *
import random

class GeoFenceManager:
    
    def __init__(self):
        self.listGeoFence = {}
        self.baseColor = 0.05
        self.deltaGroveColor = 0.05
        self.sendGetListGeoFence()
    
    def initListGeoFence(self):
        numberGeoFence = geoFenceConfig.getMaxGeoFence()
        for i in range(0, numberGeoFence):
            geoFence = GeoFence()
            self.listGeoFence[geoFence.getId()] = geoFence

    def addGeoFence(self, num):
        for i in range(num):
            geoFence = GeoFence()
            geoFence.setColorHSV(random.uniform(0, 0.5))
            self.listGeoFence[geoFence.getId()] = geoFence

    def addGeoFenceByListPoint(self, listPoint):
        msg = geoFenceController.sendInitGeoFence(listPoint)
        print(msg)
        if msg['errCode'] == 0:
            id = msg['idGeoFence']
            listServerPoint = msg['listGeoFencePoint']
            self.listGeoFence[id] = GeoFence(listServerPoint=listServerPoint, id=id)
            self.listGeoFence[id].setColorHSV(random.uniform(0.85, 1))

    def sendGetListGeoFence(self):
        msg = geoFenceController.sendGetAllGeoFence()
        if msg['errCode'] == 0:
            listId = msg['listGeoFenceUID'] 
            listPointOfGeoFence = msg['listPointOfGeoFences']
            for i in range(0, len(listId)):
                id = listId[i]
                listServerPoint = listPointOfGeoFence[i]
                self.listGeoFence[id] = GeoFence(listServerPoint=listServerPoint, id=id)
                self.listGeoFence[id].setColorHSV(random.uniform(0.85, 1))
                print(GeoFence(listServerPoint=listServerPoint, id=id))
        return

    def getGeoFenceById(self, id):
        if id in self.listGeoFence:
            return self.listGeoFence[id]
        return None

    def sendUpdateGeoFence(self, id, listInitPoint):
        if not id in self.listGeoFence:
            return
        oldGeoFence = self.listGeoFence[id]
        oldColor = oldGeoFence.getColorHSV()
        listPoint = []
        for point in listInitPoint:
            listPoint.append({'x': point.getX(), 'y': point.getY()})
        msg = geoFenceController.sendUpdateGeoFence(id, listPoint)
        if msg['errCode'] == 0:
            self.listGeoFence[id] = GeoFence(listServerPoint=msg['listGeoFencePoint'], id = msg['idGeoFence'])
            self.listGeoFence[id].setColorHSV(oldColor)

    def getGeoFenceColorById(self, id):
        if id in self.listGeoFence:
            return self.listGeoFence[id].getColorHSV()
        return None

    def getListGeoFence(self):
        return self.listGeoFence

    def deleteGeoFence(self, id):
        msg = geoFenceController.sendDeleteGeoFence(id)
        if msg['errCode'] == 0:
            self.listGeoFence = {}
            listId = msg['listGeoFenceUID'] 
            listPointOfGeoFence = msg['listPointOfGeoFences']
            for i in range(0, len(listId)):
                id = listId[i]
                listServerPoint = listPointOfGeoFence[i]
                self.listGeoFence[id] = GeoFence(listServerPoint=listServerPoint, id=id)
                self.listGeoFence[id].setColorHSV(random.uniform(0.85, 1))
                print(GeoFence(listServerPoint=listServerPoint, id=id))

