# Parámetros importantes del problema
gamma = 0.9  # Este es el factor de descuento (decide cuánto valoramos el futuro)
theta = 0.0001  # Umbral de cambio mínimo para que el algoritmo se detenga
estados = [0, 1, 2, 3]  # Los estados que tenemos (en nuestro caso, las "casillas" del tablero)
acciones = ['izquierda', 'derecha']  # Las acciones posibles: mover a la izquierda o a la derecha
recompensas = {0: -1, 1: -1, 2: 1, 3: 0}  # Las recompensas que obtenemos al estar en cada estado
transiciones = {  # Qué pasa cuando tomas una acción desde cada estado
    0: {'izquierda': 0, 'derecha': 1},  # Si estás en el estado 0 y vas a la izquierda, te quedas en 0, si vas a la derecha vas al estado 1
    1: {'izquierda': 0, 'derecha': 2},  # Lo mismo para los otros estados
    2: {'izquierda': 1, 'derecha': 3},
    3: {'izquierda': 3, 'derecha': 3}  # En este caso, el estado 3 no cambia si tomas alguna acción
}

# Inicializar los valores de los estados, los cuales comenzamos en 0
valores_estados = [0 for _ in range(len(estados))]

# Función de iteración de valores
def iteracion_de_valores():
    while True:
        delta = 0  # Para medir el cambio en los valores
        # Iteramos sobre todos los estados
        for estado in estados:
            v = valores_estados[estado]  # Guardamos el valor actual de este estado
            valores_acciones = []  # Lista donde guardaremos los valores de cada acción

            # Iteramos sobre las acciones posibles (mover a la izquierda o a la derecha)
            for accion in acciones:
                # Obtenemos el estado al que llegaríamos tomando esta acción
                siguiente_estado = transiciones[estado][accion]
                # Obtenemos la recompensa de ese estado al que llegamos
                recompensa = recompensas[siguiente_estado]
                # Calculamos el valor de tomar esta acción: recompensa inmediata + valor futuro descontado
                valores_acciones.append(recompensa + gamma * valores_estados[siguiente_estado])

            # Actualizamos el valor del estado actual con el máximo valor de las acciones posibles
            valores_estados[estado] = max(valores_acciones)

            # Medimos cuánto cambió el valor del estado en esta iteración
            delta = max(delta, abs(v - valores_estados[estado]))

        # Si el cambio es muy pequeño (menos que el umbral "theta"), dejamos de iterar
        if delta < theta:
            break

# Ejecutamos la iteración de valores
iteracion_de_valores()

# Imprimimos los valores finales de los estados
print("Valores de los estados:", valores_estados)
