#!/usr/bin/python

import math


class City:

    number_of_city = 0

    def __init__(self, name, x, y):
        self.name = str(name)
        self.x = int(x)
        self.y = int(y)


    def next_distance(self, cnext):
        dx = (self.x - cnext.x)**2
        dy = (self.y - cnext.y)**2
        result = math.sqrt(dx + dy)
        return round(result, 6)

