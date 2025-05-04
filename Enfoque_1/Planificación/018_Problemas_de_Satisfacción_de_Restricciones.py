def es_seguro(tablero, fila, col, n):
    # Comprobar la columna
    for i in range(fila):
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

def resolver_n_reinas(tablero, fila, n):
    # Si hemos colocado todas las reinas
    if fila == n:
        return True
    
    # Intentar colocar una reina en cada columna de la fila actual
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila] = col
            if resolver_n_reinas(tablero, fila + 1, n):
                return True
            tablero[fila] = -1  # Retroceder si no se encuentra una solución
    
    return False

def imprimir_tablero(tablero, n):
    for i in range(n):
        fila = ['-' for _ in range(n)]
        fila[tablero[i]] = 'S'
        print(' '.join(fila))

def n_reinas(n):
    tablero = [-1] * n  # Inicializar el tablero
    if resolver_n_reinas(tablero, 0, n):
        imprimir_tablero(tablero, n)
    else:
        print("No hay solución")

# Ejemplo: Resolver el problema de las 8 reinas
n_reinas(8)
