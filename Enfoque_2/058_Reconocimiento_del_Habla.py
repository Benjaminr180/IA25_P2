# Diccionario de estados (palabras) y observaciones (sonidos simplificados)
estados = ['hola', 'ola']
observaciones = ['h', 'o', 'l', 'a']

# Probabilidades de transición (simplificadas)
transicion = {
    'hola': {'hola': 0.8, 'ola': 0.2},
    'ola': {'hola': 0.3, 'ola': 0.7}
}

# Probabilidades de emisión (qué tan probable es escuchar cierto sonido en una palabra)
emision = {
    'hola': {'h': 0.6, 'o': 0.2, 'l': 0.1, 'a': 0.1},
    'ola': {'h': 0.1, 'o': 0.5, 'l': 0.2, 'a': 0.2}
}

# Probabilidad inicial
inicio = {'hola': 0.5, 'ola': 0.5}

# Algoritmo de Viterbi
def viterbi(obs, estados, inicio, transicion, emision):
    V = [{}]
    camino = {}

    # Paso inicial
    for estado in estados:
        V[0][estado] = inicio[estado] * emision[estado][obs[0]]
        camino[estado] = [estado]

    # Recorrer observaciones
    for t in range(1, len(obs)):
        V.append({})
        nuevo_camino = {}

        for estado_actual in estados:
            prob_estado, estado_prev = max(
                [(V[t-1][estado_ant] * transicion[estado_ant][estado_actual] * emision[estado_actual][obs[t]], estado_ant)
                 for estado_ant in estados]
            )
            V[t][estado_actual] = prob_estado
            nuevo_camino[estado_actual] = camino[estado_prev] + [estado_actual]

        camino = nuevo_camino

    # Resultado final
    prob_max, estado_final = max((V[-1][estado], estado) for estado in estados)
    return camino[estado_final], prob_max

# Ejecutar
camino, probabilidad = viterbi(observaciones, estados, inicio, transicion, emision)

# Mostrar resultado
print(" Observaciones:", observaciones)
print(" Palabra más probable:", ' → '.join(camino))
print(f" Probabilidad estimada: {probabilidad:.4f}")
