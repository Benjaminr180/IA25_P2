def busqueda_en_profundidad(grafo, nodo_inicio, nodo_objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(nodo_inicio)
    camino.append(nodo_inicio)

    if nodo_inicio == nodo_objetivo:
        return camino

    for vecino in grafo[nodo_inicio]:
        if vecino not in visitados:
            resultado = busqueda_en_profundidad(grafo, vecino, nodo_objetivo, visitados, camino)
            if resultado is not None:
                return resultado

    camino.pop()  # Si no hay camino, retrocede
    return None

# Grafo sin pesos (como el de anchura)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar búsqueda
camino = busqueda_en_profundidad(grafo, 'A', 'F')
print("Camino encontrado:", camino)
