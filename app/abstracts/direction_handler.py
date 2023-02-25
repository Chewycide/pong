import math

class DirectionHandler(object):
    """
        Uses vector math to handle 2D movement. This class needs
        to be instantiated in a straight moving object and must
        be provided a magnitude on instantiation. magnitude
        will be the speed of the object
    """
    def __init__(self, magnitude):
        self.magnitude = magnitude


    def get_xcomp(self, angle) -> float:
        return round(self.magnitude * math.cos(math.radians(angle)), 2)


    def get_ycomp(self, angle) -> float:
        return round(self.magnitude * math.sin(math.radians(angle)), 2)