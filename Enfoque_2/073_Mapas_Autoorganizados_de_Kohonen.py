import random
import math

# Distancia euclidiana entre dos vectores
def distancia(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

# Inicializa el mapa (pesos aleatorios)
def inicializar_mapa(num_neuronas, dimension_entrada):
    return [[random.random() for _ in range(dimension_entrada)] for _ in range(num_neuronas)]

# Encuentra la neurona ganadora (BMU)
def mejor_neurona(mapa, entrada):
    distancias = [distancia(neurona, entrada) for neurona in mapa]
    return distancias.index(min(distancias))

# Actualiza los pesos de la neurona ganadora y su vecindario
def actualizar_mapa(mapa, entrada, indice_ganador, tasa_aprendizaje, vecindad):
    for i, neurona in enumerate(mapa):
        if abs(i - indice_ganador) <= vecindad:
            for j in range(len(neurona)):
                neurona[j] += tasa_aprendizaje * (entrada[j] - neurona[j])

# Entrenamiento del SOM
def entrenar_som(datos, num_neuronas=5, epocas=100, tasa_aprendizaje=0.1):
    dimension_entrada = len(datos[0])
    mapa = inicializar_mapa(num_neuronas, dimension_entrada)

    for epoca in range(epocas):
        for entrada in datos:
            ganador = mejor_neurona(mapa, entrada)
            vecindad = max(1, int(num_neuronas / (epoca + 1)))  # Vecindad decrece con el tiempo
            actualizar_mapa(mapa, entrada, ganador, tasa_aprendizaje, vecindad)

    return mapa

# Datos de ejemplo (2D)
datos = [
    [0.1, 0.2],
    [0.3, 0.4],
    [0.9, 0.8],
    [0.8, 0.9],
    [0.2, 0.1]
]

mapa_entrenado = entrenar_som(datos)

print("Mapa autoorganizado final:")
for i, neurona in enumerate(mapa_entrenado):
    print(f"Neurona {i + 1}: {neurona}")
