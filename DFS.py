def test_cell(s, row, col):
    '''Dado un Sudoku, un número de fila y columna,
    devuelve una lista que representa los números válidos
    que pueden ir en esa celda.
    0=posible, 1=no posible'''
    used = [0]*10
    used[0] = 1
    block_row = row // 3
    block_col = col // 3
    #Fila y columna
    for m in range(9):
        used[s[m][col]] = 1;
        used[s[row][m]] = 1;
    #Cuadro 3x3
    for m in range(3):
        for n in range(3):
            used[s[m + block_row*3][n + block_col*3]] = 1
    return used

def initial_try(s):
    '''Dado un Sudoku, lo intenta resolver iterando a través
    de cada celda y determinar los números posibles en esa celda.
    Si solo existe un numero posible, se llena y continúa hasta
    que el sudoku se atasque'''
    stuck = False
    while not stuck:
        stuck = True
        #Iteraciones a traves del sudoku
        for row in range(9):
            for col in range(9):
                used = test_cell(s, row, col)
                #Mas de una posibilidad
                if used.count(0) != 1:
                    continue
                #Si la celda actual está vacía y solo hay una
                #posibilidad, se completa la celda actual
                for m in range(1, 10):
                    if s[row][col] == 0 and used[m] == 0:
                        s[row][col] = m
                        stuck = False
                        break

def DFS_solve(s, row, col):
    '''Dado un Sudoku, resuelve ejecutando DFS de forma recursiva.
     que prueba las posibles soluciones y mediante
     el retroceso (eliminando intentos inválidos y
     todos los posibles casos derivados de esos intentos)'''
    if row == 8 and col == 8:
        used = test_cell(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True

    if col == 9:
        row = row+1
        col = 0

    if s[row][col] == 0:
        used = test_cell(s, row, col)
        for i in range(1, 10):
            if used[i] == 0:
                s[row][col] = i
                if DFS_solve(s, row, col+1):
                    return True
        #Se prueba 1-9 sin éxito
        s[row][col] = 0
        return False
    return DFS_solve(s, row, col+1)

def DFSAlgoritmo(s):
    if len(s) == 9:
        
        #Resolucion
        initial_try(s)
        for line in s:
            if 0 in line:
                DFS_solve(s, 0, 0)
                break
        return s

if __name__ == "__main__":
    DFSAlgoritmo()
    #Arreglo con el sudoku sin resolver
    s=[[0,3,7,0,8,0,2,6,4],[0,9,5,0,2,0,0,0,3],[0,0,0,6,0,0,0,0,9],
     [5,0,9,0,0,7,0,2,1],[2,0,6,0,1,0,0,3,0],[3,0,0,9,4,0,0,0,6],
     [0,0,0,7,3,0,1,4,2],[0,0,3,0,0,4,0,0,8],[0,0,0,0,0,8,3,0,5]]
