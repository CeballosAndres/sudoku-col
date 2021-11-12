import numpy as np
import time
class Sudoku:

    def __init__(self, sudoku=None):
        if sudoku == None:
            raise NameError('Sudoku is empty')
        sudoku_array = sudoku.split(',')
        sudoku_array=[[int(val) if val != '' else 0 for val in row] for row in sudoku_array]
        self.sudoku = np.reshape(sudoku_array, (9,9))

    def dfs(self):
        time.sleep(1)
        print(self.sudoku)
        return [[val if val != '' else 'd' for val in row] for row in self.sudoku] 

    def backtracking(self):
        time.sleep(2)
        return [[val if val != '' else 'b' for val in row] for row in self.sudoku] 

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
