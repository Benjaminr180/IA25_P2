from collections import deque  # Usamos deque porque permite sacar elementos fácilmente por los dos lados (colas)

# Función principal de Búsqueda Bidireccional
def busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo):
    if nodo_inicio == nodo_objetivo:
        return [nodo_inicio]  # Caso simple, si ya estamos en el objetivo

    # Colas para explorar desde el inicio y desde el final (dos lados)
    cola_inicio = deque([[nodo_inicio]])
    cola_objetivo = deque([[nodo_objetivo]])

    # Diccionarios para guardar nodos visitados y el camino desde cada lado
    visitados_inicio = {nodo_inicio: [nodo_inicio]}
    visitados_objetivo = {nodo_objetivo: [nodo_objetivo]}

    while cola_inicio and cola_objetivo:
        #   EXPANSIÓN DESDE EL INICIO 
        camino_inicio = cola_inicio.popleft()
        actual_inicio = camino_inicio[-1]

        for vecino in grafo.get(actual_inicio, []):  # Recorremos los vecinos del nodo actual
            if vecino not in visitados_inicio:
                nuevo_camino = camino_inicio + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                # Si el nodo ya fue visitado desde el otro lado, ya encontramos el punto de conexión
                if vecino in visitados_objetivo:
                    return nuevo_camino + visitados_objetivo[vecino][-2::-1]

        # EXPANSIÓN DESDE EL OBJETIVO 
        camino_objetivo = cola_objetivo.popleft()
        actual_objetivo = camino_objetivo[-1]

        for vecino in grafo.get(actual_objetivo, []):
            if vecino not in visitados_objetivo:
                nuevo_camino = camino_objetivo + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)

                # Verificamos si ya lo visitamos desde el otro lado
                if vecino in visitados_inicio:
                    return visitados_inicio[vecino] + nuevo_camino[-2::-1]

    return None  # Si no hay conexión entre los dos nodos

#  Implementación del grafo (no dirigido) 
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#  Prueba de búsqueda 
camino = busqueda_bidireccional(grafo, 'A', 'F')
print("Camino encontrado:", camino)
