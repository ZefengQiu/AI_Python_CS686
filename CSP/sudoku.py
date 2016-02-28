#!/usr/bin/python

class Sudoku:

    def __init__(self):
        self.sudoku = []
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.rst_domain = {}        #most restricted variable domain
        self.rst_dic = {}           #most restricted variable dictionary
        self.cst_dic = {}           #most constraining variable dictionary
        #for back tracking
        self.queue = None
        self.tracking_sudoku = None
        self.tracking_var = None


    def add_row(self, row):
        self.sudoku.append(row)


    def get_neighbor(self, row, column):
        """ get all the neighbor of certain variable in sudoku """
        neighbor = []

        for i in range(0,9,1):
            if  i != row:
                neighbor.append((i,column))
            if  i != column:
                neighbor.append((row, i))

        r = row/3
        c = column/3
        for i in range(r*3, r*3+3, 1):
            for j in range(c*3, c*3+3, 1):
                if i != row and j != column:
                      neighbor.append((i,j))

        return neighbor


    def get_unassigned(self, row, column):
        """ get all the unassigned of certain variable in sudoku """
        unassigned = []
        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.sudoku[i][j] == 0:
                    if i != row or j != column:
                        unassigned.append((i,j))

        return unassigned


    def check_row(self, row, number):
        """ check whether the row contain the number """
        for n in self.sudoku[row]:
            if n == number:
                return False
        return True


    def check_column(self, column, number):
        """ check whether the column contain the number """
        for i in range(0,9,1):
            if self.sudoku[i][column] == number:
                return False
        return True


    def check_square(self, row, column, number):
        """ check whether the 3*3 square contain the number """
        r = row/3
        c = column/3
        for i in range(r*3, r*3+3, 1):
            for j in range(c*3, c*3+3, 1):
                if self.sudoku[i][j] == number:
                    return False
        return True


    def check_cst_var(self, row, column):
        """number of variable in sudoku that is empty"""
        cst = 0
        for r in self.sudoku[row]:
            if r == 0:
                cst += 1
        cst -= 1

        for c in range(0,9,1):
            if self.sudoku[c][column] == 0:
                cst += 1
        cst -= 1

        r = row/3
        c = column/3
        for i in range(r*3, r*3+3, 1):
            for j in range(c*3, c*3+3, 1):
                if self.sudoku[i][j] == 0:
                    cst += 1
        cst -= 1

        return cst


    def get_domain(self, row, column):
        """checking most restricted variable"""
        rst = []
        for number in self.domain:
            if self.check_row(row, number):
                if self.check_column(column,number):
                    if self.check_square(row, column, number):
                        rst.append(number)
        return rst



    #give out the variables,which is most restricted and most constraining
    def rst_cst_var(self):
        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.sudoku[i][j] == 0:
                    rst = self.get_domain(i,j)
                    rst_number = len(rst)
                    # self.rst_domain[(i,j)] = rst
                    self.rst_dic[(i,j)] = rst_number
                    self.cst_dic[(i,j)] = self.check_cst_var(i,j)

        tmp = []
        for w in sorted(self.rst_dic, key=self.rst_dic.get, reverse=True):
            max = 0
            if self.rst_dic[w] >= max:
                tmp.append(w)

        for w in sorted(self.cst_dic, key=self.cst_dic.get, reverse=True):
            max = 0
            if self.cst_dic[w] >= max:
                if w in tmp:
                    return w