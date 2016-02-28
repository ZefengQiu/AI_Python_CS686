#!/usr/bin/python

from queue import Queue
import copy

class Solver:

    def __init__(self, sudoku, starter):
        self.sudoku = sudoku
        self.starter = starter
        self.steps = 0


    def lst_cst_heuristic(self, var, sdk):
        """ heuristic function that give least constraining value in the domain """
        influence = {}
        queue = Queue()
        dm = sdk.get_domain(var[0], var[1])
        for v in dm:
            inf = 0
            for i in range(0,9,1):
                for j in range(0,9,1):
                    if sdk.sudoku[i][j] == 0:
                        if v in sdk.get_domain(i,j):
                            inf += 1
            influence[v] = inf

        for w in sorted(influence, key=influence.get, reverse=False):
            queue.enqueue(w)

        return queue


    def forword_check(self, value, variable, sdk_copy):
        """ implementing the backtracking algorithm """
        row = variable[0]
        column = variable[1]
        neighbor = sdk_copy.get_neighbor(row, column)
        # print "neighbor is ", neighbor
        for n in neighbor:
            if sdk_copy.sudoku[n[0]][n[1]] == value:
                return False
            if sdk_copy.sudoku[n[0]][n[1]] == 0:
                # dm = sdk_copy.rst_domain[n]
                dm = sdk_copy.get_domain(n[0],n[1])
                if value in dm:
                    dm.remove(value)
                    if not dm:
                        # print variable, "cannot assign-", value
                        return False
        return True


    def backtracking(self, variable, sdk, back):
        """ implementing the backtracking algorithm """
        if not back:
            # print "get back", sdk.queue.items
            sdk.queue = self.lst_cst_heuristic(variable, sdk)
        row = variable[0]
        column = variable[1]
        unassigned = sdk.get_unassigned(row, column)

        sdk_copy = copy.deepcopy(sdk)
        # print "backtracking", variable, sdk.queue.items

        if sdk.queue.isEmpty():
            return self.backtracking(sdk.tracking_var, sdk.tracking_sudoku, True)

        while sdk.queue.items:
            value = sdk.queue.dequeue()
            cp = copy.deepcopy(sdk_copy)
            # print sdk.queue.items
            if self.forword_check(value, variable, cp):
                #check whether satisfy the constrain
                if sdk_copy.check_row(row, value) and sdk_copy.check_column(column, value) and sdk_copy.check_square( row, column, value):
                    #assign the value to variable
                    # print variable, " assign: ", value
                    sdk_copy.sudoku[variable[0]][variable[1]] = value
                    #select an unassigned variable X
                    if len(unassigned) == 0:
                        # print "break loop"
                        return sdk_copy
                    else:
                        self.steps += 1
                        sdk_copy.tracking_sudoku = sdk
                        sdk_copy.tracking_var = variable
                        return self.backtracking(unassigned[0], sdk_copy, False)
                elif sdk.queue.isEmpty():
                    # print "go back"
                    return self.backtracking(sdk.tracking_var, sdk.tracking_sudoku, True)

            elif sdk.queue.isEmpty():
                # print "go back"
                return self.backtracking(sdk.tracking_var, sdk.tracking_sudoku, True)
            else:
                continue





    def game(self):
        # print "(3,6) ", self.sudoku.rst_domain[(3,6)]

        result = self.backtracking(self.starter, self.sudoku, False)
        return result




