# Definir los estados, acciones y observaciones
estados = ['S0', 'S1']  # Estados del entorno
acciones = ['A0', 'A1']  # Acciones posibles
observaciones = ['O0', 'O1']  # Observaciones posibles

# Recompensas
recompensas = {'S0': 5, 'S1': 10}  # Recompensas de cada estado

# Función de transición de estado (probabilidades)
P = {
    'S0': {'A0': {'S0': 0.8, 'S1': 0.2}, 'A1': {'S0': 0.5, 'S1': 0.5}},
    'S1': {'A0': {'S0': 0.3, 'S1': 0.7}, 'A1': {'S0': 0.6, 'S1': 0.4}},
}

# Función de observación (probabilidades de obtener una observación dado el estado)
Z = {
    'S0': {'A0': {'O0': 0.9, 'O1': 0.1}, 'A1': {'O0': 0.6, 'O1': 0.4}},
    'S1': {'A0': {'O0': 0.2, 'O1': 0.8}, 'A1': {'O0': 0.4, 'O1': 0.6}},
}

# Creencia inicial (probabilidades iniciales de estar en cada estado)
creencia_inicial = {'S0': 0.5, 'S1': 0.5}

# Función para actualizar la creencia del agente basado en la observación
def actualizar_creencia(creencia, accion, observacion):
    nueva_creencia = {}
    total = 0
    for estado in estados:
        probabilidad = 0
        for s in estados:
            probabilidad += P[s][accion].get(estado, 0) * Z[estado][accion].get(observacion, 0) * creencia[s]
        nueva_creencia[estado] = probabilidad
        total += probabilidad

    # Normalizar la creencia para que la suma de probabilidades sea 1
    for estado in nueva_creencia:
        nueva_creencia[estado] /= total
    
    return nueva_creencia

# Función para tomar la mejor acción basada en la creencia
def tomar_decision(creencia):
    valor_maximo = -float('inf')
    mejor_accion = None
    for accion in acciones:
        valor_accion = 0
        for estado in estados:
            valor_accion += recompensas[estado] * creencia[estado]
        if valor_accion > valor_maximo:
            valor_maximo = valor_accion
            mejor_accion = accion
    return mejor_accion

# Ejemplo de ejecución
observacion = 'O1'  # Observación recibida
accion = 'A1'  # Acción tomada

# Actualizar creencia con la observación y la acción tomadas
nueva_creencia = actualizar_creencia(creencia_inicial, accion, observacion)
print("Nueva creencia después de la observación:", nueva_creencia)

# Tomar una decisión basada en la creencia actualizada
accion_elegida = tomar_decision(nueva_creencia)
print("Mejor acción a tomar:", accion_elegida)
