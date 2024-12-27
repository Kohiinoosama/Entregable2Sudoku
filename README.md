# Entregable2Sudoku
# Sudoku Solver con Algoritmo de Backtracking

## Descripción

Este proyecto resuelve el rompecabezas de Sudoku utilizando la técnica algorítmica de **backtracking**. El Sudoku es un juego de lógica en el que se debe llenar una cuadrícula de 9x9 celdas, donde cada fila, columna y subcuadrícula de 3x3 debe contener los números del 1 al 9 sin repetirse.

Este proyecto toma un tablero de Sudoku incompleto y resuelve el rompecabezas utilizando el algoritmo de **backtracking**. El backtracking es una técnica de prueba y error en la que se toman decisiones secuenciales para encontrar una solución válida. Si una decisión no lleva a una solución, se retrocede para probar otras opciones.

## Reglas del Sudoku

Las reglas básicas del Sudoku son las siguientes:

1. **Filas**: Cada fila debe contener los números del 1 al 9 sin repetirse.
2. **Columnas**: Cada columna debe contener los números del 1 al 9 sin repetirse.
3. **Subcuadrículas 3x3**: Cada subcuadrícula 3x3 debe contener los números del 1 al 9 sin repetirse.

## Algoritmo de Backtracking

El algoritmo de backtracking para resolver el Sudoku sigue estos pasos:

1. **Buscar una celda vacía**: El algoritmo busca una celda vacía en el tablero.
2. **Probar un número**: Intenta colocar un número del 1 al 9 en la celda vacía.
3. **Verificar validez**: Si el número no viola las reglas del Sudoku (es decir, no se repite en la fila, columna ni subcuadrícula), lo coloca en la celda.
4. **Recursividad**: Luego, hace una llamada recursiva para resolver el siguiente número.
5. **Retroceso**: Si el número no es válido en alguna etapa, se retrocede y prueba otro número para la celda anterior.
6. **Finalización**: El proceso continúa hasta que todas las celdas estén llenas o se determine que no hay solución.

## Funciones del Proyecto

1. **es_valido(tablero, fila, col, num)**: Verifica si un número es válido en la celda especificada del tablero, asegurándose de que no se repita en la fila, columna ni subcuadrícula 3x3.
2. **resolver_sudoku(tablero)**: Implementa el algoritmo de backtracking. Busca celdas vacías y prueba números del 1 al 9 de manera recursiva hasta resolver el Sudoku o determinar que no tiene solución.
3. **imprimir_tablero(tablero)**: Imprime el tablero de Sudoku, mostrando un punto (.) para las celdas vacías.

## Complejidad del Algoritmo

- **Peor caso**: El algoritmo tiene una complejidad de **O(9^(n^2))** en el peor caso, donde **n** es el tamaño del tablero (en este caso, n=9).
  - Esto se debe a que el algoritmo probará todas las combinaciones posibles de números en las celdas vacías, lo que puede llevar a muchas iteraciones si el tablero tiene muchas celdas vacías.
- **Mejor caso**: En el mejor caso, cuando el tablero ya está parcialmente resuelto, la complejidad se reduce significativamente, pudiendo ser **Ω(1)** si el tablero ya está resuelto o casi completo.
