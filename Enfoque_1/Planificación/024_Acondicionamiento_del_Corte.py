import random

def calcular_conflictos(tablero, n):
    """
    Función para contar los conflictos de un tablero de N-Reinas.
    Un conflicto se considera cuando dos reinas están en la misma fila, columna o diagonal.
    """
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Verificar conflictos de columna
            if tablero[i] == tablero[j]:
                conflictos += 1
            # Verificar conflictos de diagonal
            if abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

def buscar_vecino(tablero, n):
    """
    Genera el mejor vecino posible de un tablero, es decir, el tablero con menos conflictos.
    """
    mejor_tablero = tablero[:]
    mejor_conflictos = calcular_conflictos(mejor_tablero, n)
    
    for fila in range(n):
        for columna in range(n):
            nuevo_tablero = tablero[:]
            nuevo_tablero[fila] = columna
            nuevos_conflictos = calcular_conflictos(nuevo_tablero, n)
            
            if nuevos_conflictos < mejor_conflictos:
                mejor_conflictos = nuevos_conflictos
                mejor_tablero = nuevo_tablero
                
    return mejor_tablero, mejor_conflictos

def acondicionamiento_corte(tablero, n, max_iter=1000):
    """
    Algoritmo de Búsqueda Local con acondicionamiento del corte.
    Se detiene si no se encuentra mejora después de un número máximo de iteraciones.
    """
    iteracion = 0
    while iteracion < max_iter:
        conflictos = calcular_conflictos(tablero, n)
        
        # Si no hay conflictos, encontramos la solución
        if conflictos == 0:
            print("Solución encontrada:")
            print(tablero)
            return tablero
        
        # Buscar el mejor vecino
        vecino, nuevos_conflictos = buscar_vecino(tablero, n)
        
        # Si el vecino no mejora, hacemos un corte
        if nuevos_conflictos >= conflictos:
            print(f"No se encontró mejora en la iteración {iteracion}. Cortando búsqueda.")
            return None
        
        tablero = vecino
        iteracion += 1

    print("No se encontró solución dentro del límite de iteraciones.")
    return None

# Ejemplo de uso:
n = 8  # Número de reinas
tablero_inicial = [random.randint(0, n-1) for _ in range(n)]  # Solución inicial aleatoria
acondicionamiento_corte(tablero_inicial, n)
