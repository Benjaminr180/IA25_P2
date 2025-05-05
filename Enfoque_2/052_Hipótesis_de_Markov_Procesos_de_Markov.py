import random

# Estados posibles
estados = ['Soleado', 'Nublado', 'Lluvioso']

# Matriz de transición con probabilidades constantes (estacionarias)
transiciones = {
    'Soleado': {'Soleado': 0.6, 'Nublado': 0.3, 'Lluvioso': 0.1},
    'Nublado': {'Soleado': 0.2, 'Nublado': 0.6, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.1, 'Nublado': 0.4, 'Lluvioso': 0.5}
}

# Función para seleccionar el siguiente estado
def siguiente_estado(estado_actual):
    opciones = list(transiciones[estado_actual].keys())
    probabilidades = list(transiciones[estado_actual].values())
    return random.choices(opciones, probabilidades)[0]

# Simulación de muchos pasos para observar si se estabiliza
def simular_proceso(estado_inicial, pasos):
    conteo_estados = {'Soleado': 0, 'Nublado': 0, 'Lluvioso': 0}
    estado = estado_inicial
    
    for _ in range(pasos):
        conteo_estados[estado] += 1
        estado = siguiente_estado(estado)

    total = sum(conteo_estados.values())
    distribucion = {estado: round(conteo / total, 3) for estado, conteo in conteo_estados.items()}
    
    return distribucion

# Ejecutar la simulación
estado_inicial = 'Soleado'
pasos = 10000  # Muchos pasos para ver si se estabiliza
resultado = simular_proceso(estado_inicial, pasos)

# Mostrar resultados
print(f"Distribución aproximada después de {pasos} pasos:")
for estado, prob in resultado.items():
    print(f"{estado}: {prob}")
