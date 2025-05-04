# Heurística: Distancia Manhattan
# Calcula la distancia de Manhattan entre el nodo actual y el objetivo
def heuristica(nodo, objetivo):
    x_nodo, y_nodo = nodo
    x_objetivo, y_objetivo = objetivo
    return abs(x_nodo - x_objetivo) + abs(y_nodo - y_objetivo)

# Búsqueda Voraz Primero el Mejor
# Esta función realiza la búsqueda seleccionando siempre el nodo más prometedor según la heurística
def busqueda_voraz(grafo, inicio, objetivo):
    # Cola de prioridad con el nodo y la heurística (costo estimado)
    cola = [(inicio, heuristica(inicio, objetivo))]
    visitados = set()  # Conjunto para los nodos visitados

    # Diccionario para guardar los caminos hasta los nodos
    caminos = {inicio: []}

    while cola:
        # Ordenamos por la heurística, el nodo con la menor distancia estimada se explora primero
        cola.sort(key=lambda x: x[1])
        nodo_actual, _ = cola.pop(0)

        # Si encontramos el objetivo, devolvemos el camino
        if nodo_actual == objetivo:
            return caminos[nodo_actual] + [nodo_actual]

        # Marcar el nodo como visitado
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explorar los vecinos del nodo actual
            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    # Calculamos la heurística para el vecino
                    h = heuristica(vecino, objetivo)
                    # Añadimos el vecino a la cola con su heurística
                    cola.append((vecino, h))
                    # Guardamos el camino hasta este vecino
                    caminos[vecino] = caminos[nodo_actual] + [nodo_actual]

    return None  # Si no encontramos el camino

# Grafo (usando coordenadas 2D) 
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

camino = busqueda_voraz(grafo, inicio, objetivo)
print("Camino encontrado:", camino)
