class Grafo:
    def __init__(self):
        # El grafo es un diccionario de nodos y sus conexiones (vecinos)
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        # Suponemos que el grafo es no dirigido
        if nodo1 not in self.grafo:
            self.agregar_nodo(nodo1)
        if nodo2 not in self.grafo:
            self.agregar_nodo(nodo2)
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)

    def obtener_vecinos(self, nodo):
        # Devuelve los vecinos del nodo
        return self.grafo.get(nodo, [])

# Búsqueda online: El agente solo puede ver el nodo actual y sus vecinos
def busqueda_online(grafo, inicio, objetivo):
    # Pila para la exploración (simula búsqueda en profundidad)
    pila = [inicio]
    # Conjunto para registrar los nodos visitados
    visitados = set()

    while pila:
        nodo_actual = pila.pop()

        # Si el nodo actual es el objetivo, encontramos el camino
        if nodo_actual == objetivo:
            return True
        
        # Si ya visitamos este nodo, lo ignoramos
        if nodo_actual in visitados:
            continue

        # Marcamos el nodo como visitado
        visitados.add(nodo_actual)

        # Agregamos los vecinos del nodo actual a la pila para explorarlos
        for vecino in grafo.obtener_vecinos(nodo_actual):
            if vecino not in visitados:
                pila.append(vecino)

    # Si no encontramos el objetivo, devolvemos False
    return False

# Crear el grafo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'D')
grafo.agregar_arista('D', 'E')
grafo.agregar_arista('E', 'F')

# Buscar un camino desde el nodo 'A' al nodo 'F'
resultado = busqueda_online(grafo, 'A', 'F')

print("¿Se encontró un camino de A a F?", resultado)
