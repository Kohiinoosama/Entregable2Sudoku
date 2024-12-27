# Función para verificar si un número es válido en una celda dada
def es_valido(tablero, fila, col, num):
    # Verificar si el número ya está en la fila
    for i in range(9):
        if tablero[fila][i] == num:
            return False
    
    # Verificar si el número ya está en la columna
    for i in range(9):
        if tablero[i][col] == num:
            return False
    
    # Verificar si el número ya está en el subcuadrícula 3x3
    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if tablero[i + inicio_fila][j + inicio_col] == num:
                return False
    
    return True

# Función de backtracking para resolver el Sudoku
def resolver_sudoku(tablero):
    # Buscar una celda vacía
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:  # 0 representa una celda vacía
                # Intentar con los números del 1 al 9
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        # Colocar el número
                        tablero[fila][col] = num
                        
                        # Recursivamente intentar resolver el resto del tablero
                        if resolver_sudoku(tablero):
                            return True
                        
                        # Si no se pudo, retroceder (backtrack)
                        tablero[fila][col] = 0
                return False
    return True  # Si no quedan celdas vacías, el Sudoku está resuelto

# Función para imprimir el tablero de Sudoku
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(x) if x != 0 else '.' for x in fila))

# Ejemplo de un tablero de Sudoku incompleto
tablero_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Llamada al algoritmo de backtracking
if resolver_sudoku(tablero_sudoku):
    print("¡Sudoku resuelto exitosamente!")
    imprimir_tablero(tablero_sudoku)
else:
    print("No se pudo resolver el Sudoku.")
