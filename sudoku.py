import numpy as np
import time
from DFS import *
from random import randint

class Sudoku:

    def __init__(self, sudoku=None):
        if sudoku == None:
            raise NameError('Sudoku is empty')
        sudoku_array = sudoku.split(',')
        np_sudoku = np.array(sudoku_array)
        np_sudoku[np_sudoku==''] = '0'
        int_sudoku = np_sudoku.astype('int64').reshape((9,9))
        self.sudoku = int_sudoku

    def dfs(self):
        return DFSAlgoritmo(self.sudoku)

    def backtracking(self):
        time.sleep(2)
        return [[val if val != 0 else randint(1,9) for val in row] for row in self.sudoku] 

if __name__ == "__main__":
    example = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],
        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
        ]

    sudoku = Sudoku(example)
    print(sudoku.backtraking())
