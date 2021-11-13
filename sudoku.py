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

    def genetic(self):
        raise NameError('Error in sudoku resolution')

if __name__ == "__main__":
    # Entrada esperada
    example = ",,6,8,,,,9,4,,2,,,6,,7,,,7,,,4,,2,,,,,,,,,,,1,,6,4,,,2,8,3,5,,,9,,5,,1,,,2,4,,2,6,,3,,,5,,,,,1,,,,3,8,,9,,,,1,2,"
    sudoku = Sudoku(example)
    # Salida
    print(sudoku.dfs())
