#!/usr/bin/python

class Fringe:

    queue = []

    def __init__(self, goal):
        self.goal = goal

    def addOne(self, node):
        self.queue.append(node)


    def addAll(self, neighbors):
        for node in neighbors:
            self.queue.append(node)
        return;


    def get_min_f(self):
        mini = 100000000
        if self.queue is None:
            return None

        mini_node = None

        for node in self.queue:
            if mini > node.f_value:
                mini = node.f_value
                mini_node = node

        #adding the goal city A back to unvisited city, so the expanding set is complete
        if len(mini_node.unvisited) == 0 and mini_node.city != self.goal:
            mini_node.unvisited.append(self.goal)

        return mini_node


    def print_objects(self):
        for q in self.queue:
            print "fringe now have ",len(self.queue),"-", q.city.name, q.f_value