# Heurística: Distancia Manhattan
# Esta función calcula la distancia entre un nodo y el objetivo
def heuristica(nodo, objetivo):
    x_nodo, y_nodo = nodo
    x_objetivo, y_objetivo = objetivo
    return abs(x_nodo - x_objetivo) + abs(y_nodo - y_objetivo)

# Búsqueda con Heurística: A* (simplificada)
# Esta función realiza una búsqueda informada usando la heurística de distancia Manhattan
def busqueda_con_heuristica(grafo, inicio, objetivo):
    # Cola de prioridad con el nodo, el costo acumulado y la heurística
    cola = [(0, inicio)]  # Empieza con el costo 0 y el nodo de inicio
    visitados = set()  # Conjunto para los nodos visitados

    # Diccionario para guardar los caminos
    caminos = {inicio: []}

    while cola:
        # Ordenamos por el costo total (costo real + heurística)
        cola.sort(key=lambda x: x[0])
        costo_acumulado, nodo_actual = cola.pop(0)

        # Si llegamos al objetivo, devolvemos el camino
        if nodo_actual == objetivo:
            return caminos[nodo_actual] + [nodo_actual]

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Recorremos los vecinos del nodo actual
            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    # Calculamos el costo total
                    nuevo_costo = costo_acumulado + costo
                    # Heurística: Calculamos la distancia al objetivo
                    h = heuristica(vecino, objetivo)
                    # Agregamos el vecino con el nuevo costo total (costo + heurística)
                    cola.append((nuevo_costo + h, vecino))
                    # Guardamos el camino hasta este vecino
                    caminos[vecino] = caminos[nodo_actual] + [nodo_actual]

    return None  # Si no encontramos el camino

#  Grafo (usando coordenadas 2D) 
# Los nodos son coordenadas (x, y), y el costo es 1 para moverse entre nodos
grafo = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],  # Nodo (0, 0) tiene conexiones a (0, 1) y (1, 0)
    (0, 1): [((0, 0), 1), ((1, 1), 1)],  # Nodo (0, 1) tiene conexiones a (0, 0) y (1, 1)
    (1, 0): [((0, 0), 1), ((1, 1), 1)],  # Nodo (1, 0) tiene conexiones a (0, 0) y (1, 1)
    (1, 1): [((0, 1), 1), ((1, 0), 1)]   # Nodo (1, 1) tiene conexiones a (0, 1) y (1, 0)
}

#  Prueba 
inicio = (0, 0)
objetivo = (1, 1)

camino = busqueda_con_heuristica(grafo, inicio, objetivo)
print("Camino encontrado:", camino)
