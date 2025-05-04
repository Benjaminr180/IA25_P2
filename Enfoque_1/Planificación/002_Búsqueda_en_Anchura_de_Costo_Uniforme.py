import heapq  # Cola de prioridad

def busqueda_costo_uniforme(grafo, nodo_inicio, nodo_objetivo):
    cola_prioridad = [(0, nodo_inicio)]  # (costo_total, nodo)
    padre = {nodo_inicio: None}
    costo_acumulado = {nodo_inicio: 0}

    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == nodo_objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padre[nodo_actual]
            return camino[::-1]  # Lo invertimos para que vaya desde inicio hasta objetivo

        for vecino, costo in grafo[nodo_actual]:
            nuevo_costo = costo_acumulado[nodo_actual] + costo
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
                padre[vecino] = nodo_actual

    return None  # No se encontró camino

# Grafo con pesos (costos)
grafo = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Ejecutar búsqueda
camino = busqueda_costo_uniforme(grafo, 'A', 'E')
print("Camino más barato:", camino)
