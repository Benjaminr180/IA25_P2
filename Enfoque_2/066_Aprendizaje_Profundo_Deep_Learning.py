import random
import math

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la sigmoide (para el backpropagation)
def sigmoid_derivada(x):
    return x * (1 - x)

# Entradas y salidas esperadas (compuerta AND)
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
salidas_esperadas = [0, 0, 0, 1]

# Inicializamos pesos y sesgo (bias) aleatoriamente
pesos = [random.uniform(-1, 1), random.uniform(-1, 1)]
bias = random.uniform(-1, 1)

tasa_aprendizaje = 0.1
epocas = 10000

# Entrenamiento
for epoca in range(epocas):
    for i in range(len(entradas)):
        entrada = entradas[i]
        salida_real = salidas_esperadas[i]

        # Suma ponderada
        suma = sum([entrada[j] * pesos[j] for j in range(2)]) + bias

        # Activación
        salida = sigmoid(suma)

        # Error
        error = salida_real - salida

        # Ajuste de pesos y bias
        for j in range(2):
            pesos[j] += tasa_aprendizaje * error * sigmoid_derivada(salida) * entrada[j]
        bias += tasa_aprendizaje * error * sigmoid_derivada(salida)

# Evaluación del modelo entrenado
print("Red neuronal entrenada para compuerta AND:")
for entrada in entradas:
    suma = sum([entrada[j] * pesos[j] for j in range(2)]) + bias
    salida = sigmoid(suma)
    print(f"Entrada: {entrada} => Salida: {round(salida)}")
