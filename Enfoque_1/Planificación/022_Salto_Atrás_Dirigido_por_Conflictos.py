# Función para verificar si es seguro colocar una reina en una posición dada
def es_seguro(tablero, fila, columna):
    # Verificar la columna
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True

# Función para realizar el Salto Atrás Dirigido por Conflictos
def salto_atras_dirigido_por_conflictos(tablero, fila, n, conflictos):
    if fila == n:  # Si hemos colocado todas las reinas
        return True
    for columna in range(n):
        if es_seguro(tablero, fila, columna):  # Verificamos si podemos colocar la reina
            tablero[fila] = columna  # Colocamos la reina
            conflictos[fila] = False  # Marcamos que no hay conflicto en esta fila
            if salto_atras_dirigido_por_conflictos(tablero, fila + 1, n, conflictos):  # Llamada recursiva
                return True
            tablero[fila] = -1  # Volvemos atrás si no se puede
            conflictos[fila] = True  # Marcamos que hay conflicto en esta fila
    return False

# Función para resolver el problema de las N-reinas con Salto Atrás Dirigido por Conflictos
def resolver_n_reinas_conflictos(n):
    tablero = [-1] * n  # Inicializamos el tablero con -1 (sin reinas)
    conflictos = [False] * n  # Inicializamos el arreglo de conflictos
    if salto_atras_dirigido_por_conflictos(tablero, 0, n, conflictos):
        mostrar_tablero(tablero)
    else:
        print("No hay solución")

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    n = len(tablero)
    for fila in range(n):
        fila_tablero = ['S' if i == tablero[fila] else '.' for i in range(n)]
        print(" ".join(fila_tablero))

# Llamada a la función para resolver el problema con N=8
resolver_n_reinas_conflictos(8)
