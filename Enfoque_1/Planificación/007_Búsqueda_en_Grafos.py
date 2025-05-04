from collections import deque  # Usamos deque para la cola FIFO (Primero en entrar, primero en salir)

# Esta función recorre un grafo controlando nodos ya visitados para evitar ciclos
def busqueda_en_grafos(grafo, inicio, objetivo):
    cola = deque([[inicio]])  # Cola de caminos, empezamos con solo el nodo de inicio
    visitados = set()         # Conjunto para guardar los nodos ya visitados

    while cola:
        camino = cola.popleft()         # Sacamos el primer camino de la cola
        nodo_actual = camino[-1]        # Tomamos el último nodo del camino

        if nodo_actual == objetivo:
            return camino  # Si encontramos el objetivo, regresamos el camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcamos el nodo como visitado

            # Recorremos los vecinos del nodo actual
            for vecino in grafo.get(nodo_actual, []):
                nuevo_camino = list(camino) + [vecino]  # Creamos un nuevo camino agregando el vecino
                cola.append(nuevo_camino)               # Agregamos el nuevo camino a la cola

    return None  # Si no se encuentra el objetivo

#  Grafo para probar 
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Prueba 
camino = busqueda_en_grafos(grafo, 'A', 'E')
print("Camino encontrado:", camino)
