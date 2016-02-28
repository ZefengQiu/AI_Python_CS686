#!/usr/bin/python
from min_spanning_tree import mini_tree_length

class Node:

    def __init__(self, city, came_from_node, unvisited, goal):
        self.goal = goal
        self.city = city
        self.came_from = came_from_node
        self.unvisited = unvisited
        self.f_value = 0
        self.g_value = 0


    def heuristic(self, current_city, unvisited_neighbors):
        mst = mini_tree_length()
        if len(unvisited_neighbors) < 2:
            mst_length = 0
        else:
            mst_length = mst.calculate_unvisited_node(unvisited_neighbors[:])

        return current_city.disto_unvisited(unvisited_neighbors[:]) + current_city.disto_a(self.goal, unvisited_neighbors[:]) + mst_length
        # return 0


    def g_function(self, current_city, expand_city, pre_g_value):

        return current_city.next_distance(expand_city) + pre_g_value


    def f_function(self, current_city, expand_city, unvisited_neighbors, pre_g_value):

        return self.g_function(current_city, expand_city, pre_g_value) + self.heuristic(current_city, unvisited_neighbors[:])

    def pop_came_from(self):
        return self.came_from



