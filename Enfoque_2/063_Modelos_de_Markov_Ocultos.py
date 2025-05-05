import random

# Definir los posibles estados ocultos y las observaciones
estados_ocultos = ['A', 'B']  # Ejemplo: A, B son los estados ocultos
observaciones = ['X', 'Y']  # Ejemplo: X, Y son las observaciones

# Probabilidades de transición entre estados
prob_transicion = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

# Probabilidades de emisión (probabilidad de ver una observación dada el estado)
prob_emision = {
    'A': {'X': 0.9, 'Y': 0.1},
    'B': {'X': 0.2, 'Y': 0.8}
}

# Probabilidades iniciales (probabilidad de estar en cada estado al comienzo)
prob_inicial = {'A': 0.6, 'B': 0.4}

# Función para generar una secuencia de observaciones utilizando el HMM
def generar_secuencia(num_observaciones):
    # Inicializar el estado inicial
    estado_actual = random.choices(estados_ocultos, weights=[prob_inicial['A'], prob_inicial['B']])[0]
    secuencia_observaciones = []

    # Generar la secuencia de observaciones
    for _ in range(num_observaciones):
        observacion = random.choices(observaciones, weights=[prob_emision[estado_actual]['X'], prob_emision[estado_actual]['Y']])[0]
        secuencia_observaciones.append(observacion)
        
        # Pasar al siguiente estado usando las probabilidades de transición
        estado_actual = random.choices(estados_ocultos, weights=[prob_transicion[estado_actual]['A'], prob_transicion[estado_actual]['B']])[0]
    
    return secuencia_observaciones

# Generar una secuencia de 10 observaciones
secuencia = generar_secuencia(10)

# Mostrar la secuencia generada
print("Secuencia de observaciones generada:")
print(secuencia)
