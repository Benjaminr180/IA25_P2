import random
import math

# Función para calcular la distancia euclidiana entre dos puntos
def distancia(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

# Función para asignar cada punto al centro más cercano
def asignar_clusters(puntos, centros):
    etiquetas = []
    for punto in puntos:
        distancias = [distancia(punto, centro) for centro in centros]
        etiqueta = distancias.index(min(distancias))  # Encontrar el índice del centro más cercano
        etiquetas.append(etiqueta)
    return etiquetas

# Función para actualizar los centros de los clusters
def actualizar_centros(puntos, etiquetas, k):
    nuevos_centros = []
    for i in range(k):
        # Filtrar puntos pertenecientes al cluster 'i'
        cluster_puntos = [puntos[j] for j in range(len(puntos)) if etiquetas[j] == i]
        # Calcular el centro del cluster (media de las coordenadas)
        if cluster_puntos:  # Asegurarse de que no esté vacío
            centro = [sum(coord) / len(cluster_puntos) for coord in zip(*cluster_puntos)]
            nuevos_centros.append(centro)
        else:
            nuevos_centros.append([random.uniform(0, 10), random.uniform(0, 10)])  # Si el cluster está vacío, generamos un nuevo centro aleatorio
    return nuevos_centros

# Función principal K-means
def k_means(puntos, k, max_iter=100):
    # Inicializamos los centros aleatoriamente
    centros = random.sample(puntos, k)
    
    for _ in range(max_iter):
        etiquetas = asignar_clusters(puntos, centros)  # Asignar puntos a clusters
        nuevos_centros = actualizar_centros(puntos, etiquetas, k)  # Actualizar centros
        
        if centros == nuevos_centros:  # Si los centros no cambian, hemos convergido
            break
        centros = nuevos_centros  # Actualizar centros para la siguiente iteración
    
    return centros, etiquetas

# Crear datos aleatorios
datos = []
for _ in range(10):
    datos.append([random.gauss(3, 1), random.gauss(3, 1)])  # Cluster 1
for _ in range(10):
    datos.append([random.gauss(7, 1), random.gauss(7, 1)])  # Cluster 2
for _ in range(10):
    datos.append([random.gauss(10, 1), random.gauss(1, 1)])  # Cluster 3

# Ejecutamos el algoritmo K-means con 3 clusters
k = 3
centros, etiquetas = k_means(datos, k)

# Visualización simple en consola
for i in range(k):
    print(f"Cluster {i + 1}:")
    cluster_puntos = [datos[j] for j in range(len(datos)) if etiquetas[j] == i]
    for punto in cluster_puntos:
        print(f"    {punto}")
    print(f"Centro del Cluster {i + 1}: {centros[i]}")
    print("-" * 10)
