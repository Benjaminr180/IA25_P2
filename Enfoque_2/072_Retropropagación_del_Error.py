import math
import random

# Función de activación sigmoide y su derivada
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    sx = sigmoide(x)
    return sx * (1 - sx)

# Inicializar pesos aleatorios
def inicializar_pesos(num_inputs, num_ocultas):
    pesos_entrada_oculta = [[random.uniform(-1, 1) for _ in range(num_inputs)] for _ in range(num_ocultas)]
    sesgos_oculta = [random.uniform(-1, 1) for _ in range(num_ocultas)]

    pesos_oculta_salida = [random.uniform(-1, 1) for _ in range(num_ocultas)]
    sesgo_salida = random.uniform(-1, 1)

    return pesos_entrada_oculta, sesgos_oculta, pesos_oculta_salida, sesgo_salida

# Entrenamiento con retropropagación
def entrenar(entrada, salida_esperada, tasas_aprendizaje, epocas=1000):
    lr = tasas_aprendizaje
    num_inputs = len(entrada)
    num_ocultas = 2

    # Inicializar pesos
    pesos_entrada_oculta, sesgos_oculta, pesos_oculta_salida, sesgo_salida = inicializar_pesos(num_inputs, num_ocultas)

    for _ in range(epocas):
        # --- Propagación hacia adelante ---
        net_oculta = []
        salida_oculta = []
        for i in range(num_ocultas):
            net = sum(entrada[j] * pesos_entrada_oculta[i][j] for j in range(num_inputs)) + sesgos_oculta[i]
            net_oculta.append(net)
            salida_oculta.append(sigmoide(net))

        net_salida = sum(salida_oculta[i] * pesos_oculta_salida[i] for i in range(num_ocultas)) + sesgo_salida
        salida_final = sigmoide(net_salida)

        # --- Cálculo del error ---
        error = salida_esperada - salida_final

        # --- Retropropagación (ajuste de pesos) ---
        delta_salida = error * derivada_sigmoide(net_salida)

        # Para cada neurona oculta
        delta_oculta = []
        for i in range(num_ocultas):
            delta = delta_salida * pesos_oculta_salida[i] * derivada_sigmoide(net_oculta[i])
            delta_oculta.append(delta)

        # Actualizar pesos de salida
        for i in range(num_ocultas):
            pesos_oculta_salida[i] += lr * delta_salida * salida_oculta[i]
        sesgo_salida += lr * delta_salida

        # Actualizar pesos de entrada a oculta
        for i in range(num_ocultas):
            for j in range(num_inputs):
                pesos_entrada_oculta[i][j] += lr * delta_oculta[i] * entrada[j]
            sesgos_oculta[i] += lr * delta_oculta[i]

    return salida_final

# Entrenamiento de ejemplo
entrada = [1.0, 0.0]
salida_esperada = 1.0
salida_entrenada = entrenar(entrada, salida_esperada, tasas_aprendizaje=0.5, epocas=5000)

print(f"Entrada: {entrada}")
print(f"Salida deseada: {salida_esperada}")
print(f"Salida después del entrenamiento: {salida_entrenada}")
