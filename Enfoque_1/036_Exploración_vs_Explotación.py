import random

# Parámetros del entorno
estados = ['S0', 'S1', 'S2']  # Estados posibles del entorno
acciones = ['A0', 'A1']  # Acciones que el agente puede tomar
recompensas = {'S0': 5, 'S1': 10, 'S2': 15}  # Recompensas que recibe el agente al llegar a cada estado
transiciones = {
    'S0': {'A0': 'S1', 'A1': 'S2'},  # Si el agente está en S0 y toma A0, va a S1, si toma A1 va a S2
    'S1': {'A0': 'S2', 'A1': 'S0'},  # Si está en S1 y toma A0, va a S2, si toma A1 va a S0
    'S2': {'A0': 'S0', 'A1': 'S1'},  # Si está en S2 y toma A0, va a S0, si toma A1 va a S1
}

# Parámetros de control
epsilon = 0.1  # Probabilidad de exploración (el agente tiene una probabilidad de epsilon de explorar en vez de explotar)
gamma = 0.9  # Factor de descuento (para dar menos valor a las recompensas futuras)
alpha = 0.1  # Tasa de aprendizaje (controla la velocidad con la que el agente actualiza su conocimiento)

# Inicialización de los valores Q para cada par estado-acción (valores arbitrarios inicializados a 0)
Q = {estado: {accion: 0.0 for accion in acciones} for estado in estados}

# Función para elegir una acción usando la estrategia ε-greedy
def elegir_accion(estado, epsilon):
    """
    Elige una acción para el agente basándose en la política ε-greedy:
    - Con probabilidad epsilon, se elige una acción aleatoria (exploración).
    - Con probabilidad 1 - epsilon, se elige la acción que maximiza el valor Q (explotación).
    """
    if random.uniform(0, 1) < epsilon:
        # Exploración: seleccionar una acción aleatoria
        return random.choice(acciones)
    else:
        # Explotación: seleccionar la acción con el valor Q más alto
        return max(acciones, key=lambda a: Q[estado][a])

# Función para actualizar los valores de Q usando la fórmula de Q-learning
def actualizar_Q(estado, accion, recompensa, siguiente_estado):
    """
    Actualiza el valor Q para el par (estado, acción) usando la fórmula de Q-learning:
    Q(s, a) = Q(s, a) + α * [r + γ * max_a' Q(s', a') - Q(s, a)]
    donde:
    - Q(s, a) es el valor actual de la acción a en el estado s.
    - r es la recompensa obtenida al tomar la acción a en el estado s.
    - γ es el factor de descuento.
    - max_a' Q(s', a') es el valor máximo de la siguiente acción en el estado siguiente.
    """
    # Encontrar la mejor acción en el siguiente estado (max a' Q(s', a'))
    mejor_accion = max(acciones, key=lambda a: Q[siguiente_estado][a])
    
    # Actualizar el valor Q
    Q[estado][accion] += alpha * (recompensa + gamma * Q[siguiente_estado][mejor_accion] - Q[estado][accion])

# Simulación de episodios de aprendizaje
num_episodios = 100  # Número de episodios en los que el agente va a aprender

for episodio in range(num_episodios):
    estado_actual = random.choice(estados)  # Empezamos en un estado aleatorio
    
    while True:
        # Elegir una acción utilizando la política ε-greedy
        accion = elegir_accion(estado_actual, epsilon)
        
        # Obtener el siguiente estado después de realizar la acción
        siguiente_estado = transiciones[estado_actual][accion]
        
        # Obtener la recompensa del siguiente estado
        recompensa = recompensas[siguiente_estado]
        
        # Actualizar el valor Q usando la fórmula de Q-learning
        actualizar_Q(estado_actual, accion, recompensa, siguiente_estado)
        
        # Mover al siguiente estado
        estado_actual = siguiente_estado

        # Si el agente llega al estado terminal (S2 en este caso), termina el episodio
        if estado_actual == 'S2':
            break

# Mostrar los valores de Q después de los episodios de aprendizaje
print("Valores de Q después del aprendizaje:")
for estado in estados:
    for accion in acciones:
        print(f"Q({estado}, {accion}) = {Q[estado][accion]}")
