import numpy as np

class Sudoku:

    def __init__(self, sudoku=None):
        if sudoku == None:
            raise NameError('Sudoku is empty')
        sudoku_array = sudoku.split(',')
        self.sudoku = np.reshape(sudoku_array, (9,9))
         
    def print(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in
            self.sudoku]))

    def dump(self):
        return [[val if val != '' else 1 for val in row] for row in self.sudoku] 

    def backtraking():
        pass

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
