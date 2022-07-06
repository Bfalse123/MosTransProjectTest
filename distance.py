import math
EART_RADIUS = 6371210; 
DISTANCE = 1000; 


def computeDelta(degrees):
    return math.pi / 180 * EART_RADIUS * math.cos(deg2rad(degrees))


def deg2rad(degrees):
    return degrees * math.pi / 180

def getdeltavals(longitude, latitude):
    deltaLat = computeDelta(float(latitude))
    deltaLon = computeDelta(float(longitude))
    #получить значения диапазона для долготы, широты и расстояния
    #диапазон включает в себя все значения от точки в области квадрата допустимых значений
    aroundLat = DISTANCE / deltaLat
    aroundLon = DISTANCE / deltaLon
    return (aroundLon, aroundLat)