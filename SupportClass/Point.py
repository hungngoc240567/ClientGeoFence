from re import S


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def print(self):
        print(str(self.getX()) + " " + str(self.getY()))
    
    def toString(self):
        return str(self.getX()) + " " + str(self.getY())

    def toJson(self):
        return {"x": self.x, "y": self.y}