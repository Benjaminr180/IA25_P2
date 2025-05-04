# Parámetros importantes del MDP
gamma = 0.8  # Factor de descuento
theta = 0.0001  # Umbral para el cambio mínimo
estados = [0, 1, 2]  # Estados posibles (ej. diferentes ubicaciones en una ciudad)
acciones = ['mover_izquierda', 'mover_derecha']  # Acciones posibles

# Recompensas y transiciones
recompensas = {0: 0, 1: -1, 2: 10}  # Recompensas asociadas a cada estado
transiciones = {
    0: {'mover_izquierda': 0, 'mover_derecha': 1},  # Desde el estado 0
    1: {'mover_izquierda': 0, 'mover_derecha': 2},  # Desde el estado 1
    2: {'mover_izquierda': 1, 'mover_derecha': 2},  # Desde el estado 2
}

# Valores iniciales de los estados
valores_estados = [0 for _ in range(len(estados))]

# Evaluación de valores en un MDP
def evaluacion_de_valores():
    while True:
        delta = 0
        for estado in estados:
            v = valores_estados[estado]  # Valor actual del estado
            valores_acciones = []

            # Calcular el valor de cada acción
            for accion in acciones:
                siguiente_estado = transiciones[estado][accion]
                recompensa = recompensas[siguiente_estado]
                valores_acciones.append(recompensa + gamma * valores_estados[siguiente_estado])

            # Actualizar el valor del estado con la mejor acción
            valores_estados[estado] = max(valores_acciones)
            delta = max(delta, abs(v - valores_estados[estado]))

        # Si el cambio es menor que el umbral, terminamos
        if delta < theta:
            break

# Ejecutar la evaluación de valores
evaluacion_de_valores()

# Imprimir los valores de los estados
print("Valores de los estados:", valores_estados)
