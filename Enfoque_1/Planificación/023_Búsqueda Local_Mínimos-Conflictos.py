import random

# Función para verificar los conflictos en el tablero
def contar_conflictos(tablero, fila, columna, n):
    conflictos = 0
    # Verificar si hay conflictos en la misma columna
    for i in range(fila):
        if tablero[i] == columna:  # Misma columna
            conflictos += 1
        # Verificar si hay conflictos en la misma diagonal
        if abs(tablero[i] - columna) == abs(i - fila):  # Misma diagonal
            conflictos += 1
    return conflictos

# Función principal para resolver el problema de las N-reinas con el algoritmo de Mínimos-Conflictos
def min_conflictos(n, max_iter=10000):
    # Inicialización: solución aleatoria, cada reina está en una fila diferente y en una columna aleatoria
    tablero = [random.randint(0, n-1) for _ in range(n)]
    iteraciones = 0  # Contador de iteraciones

    while iteraciones < max_iter:
        # Verificar si hemos llegado a una solución válida (sin conflictos)
        if sum(contar_conflictos(tablero, fila, tablero[fila], n) for fila in range(n)) == 0:
            mostrar_tablero(tablero)  # Mostrar la solución
            print(f"Solución encontrada en {iteraciones} iteraciones")
            return tablero
        
        # Seleccionar la fila que tiene más conflictos
        fila_conflictiva = max(range(n), key=lambda fila: contar_conflictos(tablero, fila, tablero[fila], n))
        
        # Encontrar la columna que minimiza los conflictos en esa fila conflictiva
        columna_optima = min(range(n), key=lambda col: contar_conflictos(tablero, fila_conflictiva, col, n))
        
        # Colocar la reina en la columna óptima para la fila conflictiva
        tablero[fila_conflictiva] = columna_optima
        iteraciones += 1  # Aumentar el contador de iteraciones
    
    print("No se encontró solución dentro del límite de iteraciones")
    return None

# Función para mostrar el tablero de una forma legible
def mostrar_tablero(tablero):
    n = len(tablero)
    for fila in range(n):
        fila_tablero = ['Q' if i == tablero[fila] else '.' for i in range(n)]  # 'Q' para la reina, '.' para espacio vacío
        print(" ".join(fila_tablero))

# Llamada a la función para resolver el problema de las N-reinas con N=8
min_conflictos(8)
