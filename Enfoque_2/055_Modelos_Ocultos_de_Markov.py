import random

# Estados ocultos y observaciones posibles
estados = ['Soleado', 'Lluvioso']
observaciones = ['Caminar', 'Comprar', 'Limpiar']

# Distribuciones de probabilidad
inicio = {'Soleado': 0.6, 'Lluvioso': 0.4}

transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

emision = {
    'Soleado': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1},
    'Lluvioso': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5}
}

# Simulación de una secuencia de estados y observaciones
def simular_hmm(pasos):
    secuencia_estados = []
    secuencia_obs = []

    estado = random.choices(estados, weights=[inicio[e] for e in estados])[0]

    for _ in range(pasos):
        secuencia_estados.append(estado)
        obs = random.choices(observaciones, weights=[emision[estado][o] for o in observaciones])[0]
        secuencia_obs.append(obs)
        estado = random.choices(estados, weights=[transicion[estado][s] for s in estados])[0]

    return secuencia_estados, secuencia_obs

# Ejecutamos la simulación
estados_simulados, observaciones_simuladas = simular_hmm(5)

# Mostramos los resultados
print(" Secuencia simulada:")
for i, (e, o) in enumerate(zip(estados_simulados, observaciones_simuladas), 1):
    print(f"  Paso {i}: Estado = {e}, Observación = {o}")
