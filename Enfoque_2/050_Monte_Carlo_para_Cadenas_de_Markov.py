import random

# Definir los estados y la matriz de transición
estados = ['A', 'B', 'C']
matriz_transicion = {
    'A': {'A': 0.2, 'B': 0.5, 'C': 0.3},
    'B': {'A': 0.1, 'B': 0.7, 'C': 0.2},
    'C': {'A': 0.3, 'B': 0.3, 'C': 0.4}
}

# Función que simula la transición de un estado a otro basado en la matriz de transición
def transicion_estado(estado_actual):
    transiciones = matriz_transicion[estado_actual]
    estados_posibles = list(transiciones.keys())
    probabilidades = list(transiciones.values())
    return random.choices(estados_posibles, probabilidades)[0]

# Simulación de Monte Carlo para la cadena de Markov
def monte_carlo_markov(estado_inicial, num_iteraciones):
    secuencia_estados = [estado_inicial]
    estado_actual = estado_inicial
    
    for _ in range(num_iteraciones):
        estado_siguiente = transicion_estado(estado_actual)
        secuencia_estados.append(estado_siguiente)
        estado_actual = estado_siguiente
    
    return secuencia_estados

# Ejecutar la simulación con un estado inicial
estado_inicial = 'A'
num_iteraciones = 10
secuencia_simulada = monte_carlo_markov(estado_inicial, num_iteraciones)

# Mostrar la secuencia de estados generada
print(f"Secuencia simulada de estados a partir de '{estado_inicial}':")
print(secuencia_simulada)
