import random

# Definición de los estados y recompensas
estados = ['S0', 'S1', 'S2', 'S3']  # Estados posibles
recompensas = {'S0': 0, 'S1': 1, 'S2': 2, 'S3': 3}  # Recompensas para cada estado

# Política fija: el agente sigue siempre una acción que lo lleva de un estado a otro
politica = {'S0': 'S1', 'S1': 'S2', 'S2': 'S3', 'S3': 'S0'}

# Inicialización de las funciones de valor para los estados
valor_estados = {estado: 0.0 for estado in estados}

# Número de episodios para la simulación
num_episodios = 1000
gamma = 0.9  # Factor de descuento

# Función para simular un episodio
def simular_episodio():
    episodio = []
    estado = 'S0'  # El episodio comienza en el estado S0
    while estado != 'S3':  # El episodio termina cuando llegamos al estado S3
        accion = politica[estado]  # Acción según la política
        recompensa = recompensas[estado]  # Recompensa del estado
        episodio.append((estado, recompensa))  # Guardamos el estado y la recompensa
        estado = accion  # El agente pasa al siguiente estado según la política
    episodio.append(('S3', recompensas['S3']))  # El último estado con su recompensa
    return episodio

# Algoritmo de Monte Carlo para estimar la función de valor
for episodio in range(num_episodios):
    episodio_simulado = simular_episodio()
    recompensa_acumulada = 0
    # Actualizamos el valor de los estados en el episodio
    for estado, recompensa in reversed(episodio_simulado):
        recompensa_acumulada = recompensa + gamma * recompensa_acumulada
        valor_estados[estado] += recompensa_acumulada

# Promediamos los valores para estabilizarlos
for estado in valor_estados:
    valor_estados[estado] /= num_episodios

# Mostrar los resultados finales
print("Valores estimados para cada estado después de", num_episodios, "episodios:")
for estado, valor in valor_estados.items():
    print(f"Estado {estado}: {valor:.2f}")
