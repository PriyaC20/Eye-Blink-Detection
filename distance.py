import math

def distance_calc(point1 , point2):
    val = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
    dist = math.sqrt(val)
    return dist