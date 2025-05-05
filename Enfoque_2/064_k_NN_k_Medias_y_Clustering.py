import random
import math

# 1. Implementación de k-NN (k-Vecinos más cercanos)
def distancia_euclidiana(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def knn(datos_entrenamiento, etiquetas, punto, k):
    distancias = []
    for i, punto_entrenado in enumerate(datos_entrenamiento):
        dist = distancia_euclidiana(punto_entrenado, punto)
        distancias.append((dist, etiquetas[i]))
    
    distancias.sort(key=lambda x: x[0])  # Ordenar por distancia
    vecinos = distancias[:k]  # Tomar los k vecinos más cercanos
    
    # Clasificación por mayoría
    clases = [etiqueta for _, etiqueta in vecinos]
    return max(set(clases), key=clases.count)

# 2. Implementación de k-Medias
def kmedias(datos, k, iteraciones=100):
    centroides = random.sample(datos, k)  # Elegir k puntos aleatorios como centroides
    for _ in range(iteraciones):
        # Asignar cada punto al centroide más cercano
        clusters = {i: [] for i in range(k)}
        for punto in datos:
            distancias = [distancia_euclidiana(punto, centroide) for centroide in centroides]
            cluster = distancias.index(min(distancias))  # Cluster con la distancia mínima
            clusters[cluster].append(punto)
        
        # Recalcular los centroides
        for i in range(k):
            if clusters[i]:
                centroides[i] = [sum(coord) / len(coord) for coord in zip(*clusters[i])]
    return centroides, clusters

# 3. Algoritmo de Clustering simple (Similar a k-Medias)
def clustering_simple(datos, k, iteraciones=10):
    centroides = random.sample(datos, k)  # Iniciar con k puntos aleatorios
    for _ in range(iteraciones):
        clusters = {i: [] for i in range(k)}
        for punto in datos:
            distancias = [distancia_euclidiana(punto, centroide) for centroide in centroides]
            cluster = distancias.index(min(distancias))  # Asignar al cluster más cercano
            clusters[cluster].append(punto)
        
        # Recalcular centroides como la media de los puntos en cada cluster
        for i in range(k):
            if clusters[i]:
                centroides[i] = [sum(coord) / len(coord) for coord in zip(*clusters[i])]
    return centroides, clusters

# Ejemplo de uso

# Datos de ejemplo (puntos en un espacio 2D)
datos = [
    [1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 7], [10, 12]
]
etiquetas = ['A', 'A', 'A', 'B', 'B', 'B', 'C']

# 1. k-NN
punto_a_clasificar = [5, 6]
k = 3
etiqueta_predicha = knn(datos, etiquetas, punto_a_clasificar, k)
print(f"Predicción de k-NN para el punto {punto_a_clasificar}: {etiqueta_predicha}")

# 2. k-Medias (Clustering)
k = 2
centroides, clusters = kmedias(datos, k)
print(f"Centroides de los clusters (k-Medias): {centroides}")
print(f"Clustering resultante: {clusters}")

# 3. Clustering simple
centroides, clusters = clustering_simple(datos, k)
print(f"Centroides del clustering simple: {centroides}")
print(f"Clustering simple resultante: {clusters}")
