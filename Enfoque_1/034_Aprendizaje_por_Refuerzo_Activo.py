import random

# Definimos los estados y las acciones
estados = ['S0', 'S1', 'S2']
acciones = ['A0', 'A1']

# Recompensas asociadas a cada estado
recompensas = {'S0': 0, 'S1': 1, 'S2': 10}

# Función de transición de estado: cómo cambian los estados con las acciones
transiciones = {
    'S0': {'A0': 'S1', 'A1': 'S2'},
    'S1': {'A0': 'S2', 'A1': 'S0'},
    'S2': {'A0': 'S0', 'A1': 'S1'}
}

# Inicializamos la tabla Q, que tiene un valor para cada combinación de estado y acción
Q = {estado: {accion: 0.0 for accion in acciones} for estado in estados}

# Parámetros del Q-Learning
gamma = 0.9  # Factor de descuento (consideración de recompensas futuras)
alpha = 0.1  # Tasa de aprendizaje
epsilon = 0.1  # Probabilidad de explorar
num_episodios = 1000  # Número de episodios de aprendizaje

# Función para seleccionar la acción con la estrategia epsilon-greedy
def seleccionar_accion(estado):
    if random.uniform(0, 1) < epsilon:
        # Exploración: tomamos una acción aleatoria
        return random.choice(acciones)
    else:
        # Explotación: tomamos la acción con el valor Q más alto
        return max(Q[estado], key=Q[estado].get)

# Función para actualizar la tabla Q
def actualizar_Q(estado, accion, recompensa, siguiente_estado):
    # Estimación del valor de la siguiente acción posible
    max_q_siguiente = max(Q[siguiente_estado].values())
    
    # Actualizamos el valor Q con la fórmula de Q-learning
    Q[estado][accion] += alpha * (recompensa + gamma * max_q_siguiente - Q[estado][accion])

# Ejecutamos el proceso de aprendizaje
for episodio in range(num_episodios):
    estado = 'S0'  # Comenzamos desde el estado S0
    while estado != 'S2':  # El episodio termina cuando llegamos al estado S2
        accion = seleccionar_accion(estado)  # Elegimos una acción según la estrategia
        siguiente_estado = transiciones[estado][accion]  # Obtenemos el siguiente estado
        recompensa = recompensas[estado]  # Recompensa del estado actual
        actualizar_Q(estado, accion, recompensa, siguiente_estado)  # Actualizamos la tabla Q
        estado = siguiente_estado  # Pasamos al siguiente estado

# Mostramos los valores Q después del aprendizaje
print("Tabla Q después del aprendizaje:")
for estado in Q:
    for accion in Q[estado]:
        print(f"Q({estado}, {accion}): {Q[estado][accion]:.2f}")
