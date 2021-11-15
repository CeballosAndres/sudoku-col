""" Función que recibe una matriz sudoku y retorna su resolución"""
def resolve_backtracking(tablero):
    resolver(tablero)
    return tablero

 
""" Función encargada de encontrar los espacios que se encuentren disponibles """
def hallarVacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return i, j
    return None


""" Punto de netrada: Función encargada de ingresar los números faltantes """
def resolver(tablero):
    find = hallarVacio(tablero)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validar(tablero, i, (row, col)):
            tablero[row][col] = i

            if resolver(tablero):
                return True

            tablero[row][col] = 0

    return False


""" Función encargada de validar que los números se estén ingresando en las posiciones correctas """
def validar(tablero, numero, posicion):
    if (checkFila(tablero, numero, posicion) and
            checkCol(tablero, numero, posicion) and
            checkCuadro(tablero, numero, posicion)):
        return True
    return False


""" Función encargada de verificar las filas del sudoku """
def checkFila(tablero, numero, posicion):
    for i in range(len(tablero[0])):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False
    return True


""" Función encargada de verificar las columnas del sudoku """
def checkCol(tablero, numero, posicion):
    for i in range(len(tablero)):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False
    return True


""" Función encargada de verificar los cuadrados de 3x3 que forman parte del sudoku """
def checkCuadro(tablero, numero, posicion):
    cuadro_x = posicion[1] // 3
    cuadro_y = posicion[0] // 3

    for i in range(cuadro_y * 3, cuadro_y * 3 + 3):
        for j in range(cuadro_x * 3, cuadro_x * 3 + 3):
            if tablero[i][j] == numero and (i, j) != posicion:
                return False
    return True


""" Función que mostrará el tablero en pantalla """
def mostrarTablero(tablero):
    for i in range(len(tablero)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(tablero[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")


if __name__ == "__main__":

    example = [
        [0,0,5,0,2,0,0,0,8],
        [8,0,2,0,0,9,0,6,0],
        [0,0,3,8,0,0,2,0,0],
        [0,0,0,0,4,0,0,0,0],
        [5,0,0,0,0,3,0,4,0],
        [0,0,0,2,7,0,0,0,0],
        [4,9,0,0,6,2,0,7,0],
        [0,0,0,0,9,4,6,1,2],
        [2,0,6,0,0,8,3,0,4]
    ]

    """ Invocando las funciones para mostrar el sudoku en pantalla, tanto el original como el resuelto """
    print("El sudoku propuesto es: \n")
    mostrarTablero(example)
    resolver(example)
    print("________________________________")
    print("El sudoku resuelto es: \n")
    mostrarTablero(example)
