def es_seguro(tablero, fila, col, n):
    # Verificar la columna
    for i in range(fila):
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

def resolver_n_reinas(tablero, fila, n):
    # Si todas las reinas han sido colocadas correctamente
    if fila == n:
        return True
    
    # Probar con cada columna de la fila actual
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila] = col  # Colocamos una reina en la columna actual
            if resolver_n_reinas(tablero, fila + 1, n):  # Llamada recursiva a la siguiente fila
                return True
            tablero[fila] = -1  # Retroceder si no es posible (backtrack)
    
    return False

def imprimir_tablero(tablero, n):
    # Imprimir la solución en forma de tablero
    for i in range(n):
        fila = ['.' for _ in range(n)]
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
