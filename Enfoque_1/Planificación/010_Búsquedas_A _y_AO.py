# Heurística: Distancia Manhattan
def heuristica(nodo, objetivo):
    x_nodo, y_nodo = nodo
    x_objetivo, y_objetivo = objetivo
    return abs(x_nodo - x_objetivo) + abs(y_nodo - y_objetivo)

# Algoritmo A*
def algoritmo_a_star(grafo, inicio, objetivo):
    # Cola de prioridad (conjunto de nodos a explorar) y sus costos F
    abierta = [(inicio, 0 + heuristica(inicio, objetivo))]
    # Diccionarios para almacenar los costos acumulados y los caminos
    g_costos = {inicio: 0}  # Costo real desde el inicio
    padres = {inicio: None}  # Para reconstruir el camino

    while abierta:
        # Ordenamos por el costo total F = G + H
        abierta.sort(key=lambda x: x[1])
        nodo_actual, _ = abierta.pop(0)

        # Si llegamos al objetivo, reconstruimos el camino
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]  # Invertimos el camino para mostrarlo desde el inicio

        # Expansión de vecinos
        for vecino, costo in grafo.get(nodo_actual, []):
            g_nuevo = g_costos[nodo_actual] + costo  # Cálculo del nuevo costo
            # Si es un mejor camino o el vecino no ha sido visitado
            if vecino not in g_costos or g_nuevo < g_costos[vecino]:
                g_costos[vecino] = g_nuevo
                f_nuevo = g_nuevo + heuristica(vecino, objetivo)
                abierta.append((vecino, f_nuevo))
                padres[vecino] = nodo_actual

    return None  # Si no se encuentra un camino

#  Grafo (usando coordenadas 2D) 
# Los nodos son coordenadas (x, y), y el costo es 1 para moverse entre nodos
grafo = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],  # Nodo (0, 0) tiene conexiones a (0, 1) y (1, 0)
    (0, 1): [((0, 0), 1), ((1, 1), 1)],  # Nodo (0, 1) tiene conexiones a (0, 0) y (1, 1)
    (1, 0): [((0, 0), 1), ((1, 1), 1)],  # Nodo (1, 0) tiene conexiones a (0, 0) y (1, 1)
    (1, 1): [((0, 1), 1), ((1, 0), 1)]   # Nodo (1, 1) tiene conexiones a (0, 1) y (1, 0)
}

# Prueba 
inicio = (0, 0)
objetivo = (1, 1)

camino = algoritmo_a_star(grafo, inicio, objetivo)
print("Camino encontrado:", camino)
# Algoritmo AO* simplificado para grafos OR
def algoritmo_ao_star(grafo, inicio, objetivo):
    abierta = [(inicio, 0 + heuristica(inicio, objetivo))]
    g_costos = {inicio: 0}
    padres = {inicio: None}

    while abierta:
        abierta.sort(key=lambda x: x[1])
        nodo_actual, _ = abierta.pop(0)

        if nodo_actual == objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]

        for vecino, costo in grafo.get(nodo_actual, []):
            g_nuevo = g_costos[nodo_actual] + costo
            if vecino not in g_costos or g_nuevo < g_costos[vecino]:
                g_costos[vecino] = g_nuevo
                f_nuevo = g_nuevo + heuristica(vecino, objetivo)
                abierta.append((vecino, f_nuevo))
                padres[vecino] = nodo_actual

    return None  # Si no se encuentra un camino

#  Grafo de ejemplo
grafo_ao = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

#  Prueba 
camino = algoritmo_ao_star(grafo_ao, (0, 0), (1, 1))
print("Camino encontrado:", camino)
