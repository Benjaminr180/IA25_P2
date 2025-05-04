# Diccionario que representa un grafo con utilidades (beneficios) entre nodos
grafo_utilidades = {
    'A': {'B': 5, 'C': 2},  # A tiene caminos a B (utilidad 5) y a C (utilidad 2)
    'B': {'D': 6},
    'C': {'D': 8},
    'D': {}  # Nodo final sin vecinos
}

# Función de búsqueda de utilidad máxima
def buscar_utilidad_maxima(grafo, inicio, fin):
    # Variables para guardar la mejor ruta y la mayor utilidad encontrada
    mejor_ruta = []
    mayor_utilidad = float('-inf')  # Iniciamos con la utilidad más baja posible

    # Función recursiva (DFS modificada) que recorre el grafo
    def dfs(nodo_actual, ruta_actual, utilidad_acumulada):
        nonlocal mejor_ruta, mayor_utilidad

        # Si llegamos al destino, verificamos si esta ruta es mejor
        if nodo_actual == fin:
            if utilidad_acumulada > mayor_utilidad:
                mayor_utilidad = utilidad_acumulada
                mejor_ruta = ruta_actual.copy()
            return

        # Recorremos los vecinos del nodo actual
        for vecino, utilidad in grafo[nodo_actual].items():
            ruta_actual.append(vecino)
            dfs(vecino, ruta_actual, utilidad_acumulada + utilidad)
            ruta_actual.pop()  # Retroceso para explorar otros caminos

    dfs(inicio, [inicio], 0)
    return mejor_ruta, mayor_utilidad

# Ejemplo de uso
inicio = 'A'
fin = 'D'
ruta, utilidad = buscar_utilidad_maxima(grafo_utilidades, inicio, fin)
print(f"Ruta con mayor utilidad: {ruta}, Utilidad total: {utilidad}")
