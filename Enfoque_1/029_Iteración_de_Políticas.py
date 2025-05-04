# Parámetros importantes del problema
gamma = 0.9  # Este es el factor de descuento
theta = 0.0001  # Umbral de cambio mínimo para que el algoritmo se detenga
estados = [0, 1, 2, 3]  # Los estados posibles
acciones = ['izquierda', 'derecha']  # Las acciones posibles
recompensas = {0: -1, 1: -1, 2: 1, 3: 0}  # Recompensas por cada estado
transiciones = {  # Definición de los estados a los que se puede llegar con cada acción
    0: {'izquierda': 0, 'derecha': 1},
    1: {'izquierda': 0, 'derecha': 2},
    2: {'izquierda': 1, 'derecha': 3},
    3: {'izquierda': 3, 'derecha': 3}
}

# Inicializar los valores de los estados y las políticas
valores_estados = [0 for _ in range(len(estados))]
politica = ['izquierda' for _ in range(len(estados))]  # Política inicial aleatoria

# Evaluación de la política
def evaluacion_de_politica():
    while True:
        delta = 0  # Para medir el cambio en los valores
        for estado in estados:
            v = valores_estados[estado]  # Guardamos el valor actual del estado
            accion = politica[estado]  # Acción según la política actual
            siguiente_estado = transiciones[estado][accion]  # Estado al que llegamos
            recompensa = recompensas[siguiente_estado]  # Recompensa por estar en ese estado
            # Actualizamos el valor del estado usando la política
            valores_estados[estado] = recompensa + gamma * valores_estados[siguiente_estado]
            delta = max(delta, abs(v - valores_estados[estado]))
        
        if delta < theta:  # Si el cambio es pequeño, terminamos
            break

# Mejora de la política
def mejora_de_politica():
    politica_cambiada = False
    for estado in estados:
        mejor_accion = None
        mejor_valor = float('-inf')
        # Comprobamos cuál es la mejor acción
        for accion in acciones:
            siguiente_estado = transiciones[estado][accion]
            recompensa = recompensas[siguiente_estado]
            valor_accion = recompensa + gamma * valores_estados[siguiente_estado]
            # Si esta acción da un mejor valor, la tomamos
            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion
        # Si la política cambia, actualizamos
        if politica[estado] != mejor_accion:
            politica[estado] = mejor_accion
            politica_cambiada = True

    return politica_cambiada

# Iteración de políticas
def iteracion_de_politicas():
    while True:
        # Paso 1: Evaluación de la política
        evaluacion_de_politica()
        # Paso 2: Mejora de la política
        if not mejora_de_politica():
            break

# Ejecutamos la iteración de políticas
iteracion_de_politicas()

# Imprimimos los resultados finales
print("Política final:", politica)
print("Valores de los estados:", valores_estados)
