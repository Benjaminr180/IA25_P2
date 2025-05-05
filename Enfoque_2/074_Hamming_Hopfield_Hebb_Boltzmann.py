#Código de Hamming:
import random
def hamming(patron_entrada, patron_neurona):
    # Calcula la distancia Hamming entre dos patrones
    return sum([1 for a, b in zip(patron_entrada, patron_neurona) if a != b])

def red_hamming(datos, num_neuronas):
    # Inicialización de las neuronas de la red
    neuronas = [[random.choice([0, 1]) for _ in range(len(datos[0]))] for _ in range(num_neuronas)]
    
    # Proceso de entrenamiento
    for _ in range(10):  # Iteramos varias veces
        for patron in datos:
            distancias = [hamming(patron, neurona) for neurona in neuronas]
            ganador = distancias.index(min(distancias))
            # Actualizamos la neurona ganadora
            neuronas[ganador] = patron
            
    return neuronas

# Datos binarios de ejemplo
datos_hamming = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 0, 1]
]

# Número de neuronas en la red
neurona_hamming = red_hamming(datos_hamming, 3)
print("Neuronas de la red Hamming:", neurona_hamming)

#Código de Hopfield
class RedHopfield:
    def __init__(self, num_neuronas):
        self.num_neuronas = num_neuronas
        self.matriz_energia = [[0] * num_neuronas for _ in range(num_neuronas)]
        
    def entrenamiento(self, patrones):
        for p in patrones:
            for i in range(self.num_neuronas):
                for j in range(self.num_neuronas):
                    if i != j:
                        self.matriz_energia[i][j] += p[i] * p[j]

    def actualizar(self, patrones):
        estado = patrones[:]
        for i in range(self.num_neuronas):
            suma = sum(self.matriz_energia[i][j] * estado[j] for j in range(self.num_neuronas))
            estado[i] = 1 if suma > 0 else -1
        return estado

# Datos de entrada para Hopfield (patrones de entrenamiento)
patrones_hopfield = [
    [1, -1, 1],
    [-1, 1, -1]
]

# Red Hopfield
red_hopfield = RedHopfield(3)
red_hopfield.entrenamiento(patrones_hopfield)

# Realizamos una actualización de los estados
estado_inicial = [1, -1, -1]
estado_actualizado = red_hopfield.actualizar(estado_inicial)
print("Estado actualizado de la red Hopfield:", estado_actualizado)

#Código de Hebb
def hebb(patron_entrada, tasa_aprendizaje=0.1):
    # Inicializamos los pesos a cero
    pesos = [0] * len(patron_entrada)
    for i in range(len(patron_entrada)):
        # Actualizamos los pesos usando la regla de Hebb
        pesos[i] += tasa_aprendizaje * patron_entrada[i] ** 2
    return pesos

# Datos de ejemplo
patron_hebb = [1, -1, 1]
pesos_hebb = hebb(patron_hebb)
print("Pesos después de la regla de Hebb:", pesos_hebb)

#Código de Red Boltzmann
import random

def energia_red_boltzmann(entradas, pesos):
    # Calcula la energía de la red
    energia = sum(entradas[i] * pesos[i] for i in range(len(entradas)))
    return energia

def red_boltzmann(patrones, iteraciones=1000):
    # Inicializamos pesos aleatorios
    pesos = [random.random() for _ in range(len(patrones[0]))]
    
    for _ in range(iteraciones):
        patron = random.choice(patrones)
        energia = energia_red_boltzmann(patron, pesos)
        
        # Actualizamos pesos con una simple función de energía
        for i in range(len(patron)):
            pesos[i] += random.random() * (energia - sum(patron))
            
    return pesos

# Datos de ejemplo
patrones_boltzmann = [
    [1, -1, 1],
    [-1, 1, -1]
]

# Red Boltzmann
pesos_boltzmann = red_boltzmann(patrones_boltzmann)
print("Pesos después de la red Boltzmann:", pesos_boltzmann)

