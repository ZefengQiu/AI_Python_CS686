#!/usr/bin/python

import math

class City:

    #define city class instance variable
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)


    #calculate the distance to next going city
    def next_distance(self, city_next):
        dx = (self.x - city_next.x)**2
        dy = (self.y - city_next.y)**2
        return math.sqrt(dx + dy)


    #give distance to nearest unvisited city
    def disto_unvisited(self, unvisited_cities):
        min_dis = 100000000
        if len(unvisited_cities) == 0:
            return 0
        for city in unvisited_cities:
            tmp_dis = self.next_distance(city)
            if tmp_dis < min_dis and tmp_dis != 0:
                min_dis = tmp_dis
        return min_dis


    #give nearest distance from an unvistied city to start city A
    def disto_a(self, city_a, unvisited):
        min_dis = 1000000000
        #unvisited here should be list of city class
        if len(unvisited) == 0:
            return 0
        for city in unvisited:
            dis = city.next_distance(city_a)
            if min_dis > dis and dis != 0:
                min_dis = dis
        return min_dis







