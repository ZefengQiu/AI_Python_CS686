#!/usr/bin/python
from sudoku import Sudoku
from solver import Solver

import sys
import matplotlib.pyplot as plt

def csp_sdk(folder, instance):

    fo = open("problems/%d/%d.sd"%(folder,instance), "rw+")
    sys.setrecursionlimit(1000000)
    sudoku = Sudoku()

    for line in fo:
        l = line.split()
        tmp = []
        for i in l:
            tmp.append(int(i))
        if l:
            sudoku.add_row(tmp)

    fo.close()

    starter = sudoku.rst_cst_var()
    csp = Solver(sudoku, starter)
    result = csp.game()

    for l in result.sudoku:
        print l

    del sudoku

    print("\n")
    return csp.steps


def main():

    x = []
    for i in range(1,72,1):
        x.append(i)

    # folder = 2
    # instance = 3

    for folder in range(35,72,1):
        steps = 0
        for instance in range(1,11,1):
            stp = csp_sdk(folder, instance)
            steps = steps + stp
            # y.append(steps/10.0)
            # print "average ", stp
            # print "finishing run all instance in: ", folder, " folder."

    y = [100.2, 311.5, 98.3, 92.3, 124, 245.5, 153.6, 191.9, 117.9, 389.4,
          407.0, 155.7, 280.9, 2171.5, 1236.5, 1865.2, 569.1, 451.9, 785.8, 359.9,
          694.1, 782.4, 1369.2, 323.9, 1842.3, 2664.2, 1717.2, 340.2, 739, 1177.5,
          238.6, 643.2, 176.8, 278.6, 219.7, 198.6, 200.6, 135.9, 119.4, 63.3,
          54.8, 71.3, 68.2, 59.8, 48.4, 35.0, 38.0, 34.0, 33.1, 34.1, 33.5,
          29.3, 30.7, 26.1, 25.0, 24.0, 23.3, 22.3, 21.2, 21.8, 19.0, 18.0,
          17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0]


    plt.plot(x, y)
    plt.show()



if __name__ == "__main__":
    main()