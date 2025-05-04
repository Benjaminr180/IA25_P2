from collections import deque  # Importamos la cola doble

def busqueda_en_anchura(grafo, nodo_inicio, nodo_objetivo):
    cola = deque([nodo_inicio])        # Cola con el nodo inicial
    visitados = set()                  # Conjunto de nodos ya visitados
    padre = {nodo_inicio: None}        # Diccionario para reconstruir el camino

    while cola:
        nodo_actual = cola.popleft()   # Sacamos el primero de la cola

        if nodo_actual == nodo_objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padre[nodo_actual]
            return camino[::-1]        # Invertimos el camino para mostrarlo del inicio al final

        visitados.add(nodo_actual)     # Marcamos el nodo como visitado

        for vecino in grafo[nodo_actual]:  # Recorremos sus vecinos
            if vecino not in visitados and vecino not in cola:
                cola.append(vecino)
                padre[vecino] = nodo_actual

    return None  # Si no se encontró camino

# Definimos un grafo como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecutamos la búsqueda
camino_encontrado = busqueda_en_anchura(grafo, 'A', 'D')
print("Camino encontrado:", camino_encontrado)
