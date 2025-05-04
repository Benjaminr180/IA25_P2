# Función que realiza la comprobación hacia delante
def comprobacion_hacia_delante(nodos, colores, asignaciones):
    """
    Verifica si la asignación actual es válida.
    La función recorre todas las asignaciones y comprueba si hay algún conflicto
    de color con los nodos vecinos.
    """
    for nodo, color in asignaciones.items():  # Recorre todas las asignaciones de nodos
        for vecino in nodos[nodo]:  # Recorre los vecinos del nodo actual
            if vecino in asignaciones and asignaciones[vecino] == color:  # Si un vecino tiene el mismo color
                return False  # Hay un conflicto de color con un vecino
    return True  # Si no hay conflictos, la asignación es válida

# Función recursiva de backtracking con comprobación hacia delante
def asignar_colores(nodos, colores, asignaciones):
    """
    Asigna colores a los nodos usando backtracking con comprobación hacia delante.
    Esta función recursiva prueba asignar colores a los nodos del grafo.
    Si en cualquier paso, la asignación no es válida, retrocede.
    """
    # Si todos los nodos están asignados, hemos encontrado una solución
    if len(asignaciones) == len(nodos):  # Comprobamos si ya se asignaron todos los nodos
        return asignaciones  # Si sí, retornamos la asignación completa
    
    # Elegir un nodo no asignado
    for nodo in nodos:  # Recorremos los nodos del grafo
        if nodo not in asignaciones:  # Si el nodo no ha sido asignado aún
            # Probar con cada color disponible
            for color in colores:  # Probar con cada color
                asignaciones[nodo] = color  # Asignamos el color al nodo
                if comprobacion_hacia_delante(nodos, colores, asignaciones):  # Verificamos si es una asignación válida
                    # Si es válida, continuamos con la asignación recursiva
                    resultado = asignar_colores(nodos, colores, asignaciones)
                    if resultado:  # Si encontramos una solución válida en la recursión
                        return resultado
                del asignaciones[nodo]  # Si no encontramos una solución, deshacemos la asignación para intentar otro color
    
    return None  # Si no encontramos solución, retornamos None

# Ejemplo de grafo representado como un diccionario
nodos = {
    'A': ['B', 'C'],  # Nodo A está conectado con B y C
    'B': ['A', 'C'],  # Nodo B está conectado con A y C
    'C': ['A', 'B']   # Nodo C está conectado con A y B
}

# Lista de colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Diccionario vacío para almacenar la asignación de colores
asignaciones = {}

# Ejecutamos el algoritmo para asignar colores a los nodos
resultado = asignar_colores(nodos, colores, asignaciones)

# Imprimimos el resultado final, que puede ser la asignación de colores o un mensaje de que no hay solución
if resultado:
    print("Asignación de colores exitosa:", resultado)
else:
    print("No se encontró solución")
