# Estados y observaciones
estados = ['Soleado', 'Lluvioso']
observaciones = ['Caminar', 'Comprar', 'Limpiar']
observada = ['Caminar', 'Comprar', 'Limpiar']

# Probabilidad inicial
inicio = {'Soleado': 0.6, 'Lluvioso': 0.4}

# Transición entre estados
transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Emisión de observaciones
emision = {
    'Soleado': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1},
    'Lluvioso': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5}
}

# Algoritmo Forward
def forward(obs):
    f = [{}]
    for estado in estados:
        f[0][estado] = inicio[estado] * emision[estado][obs[0]]
    
    for t in range(1, len(obs)):
        f.append({})
        for estado in estados:
            f[t][estado] = sum(f[t-1][prev] * transicion[prev][estado] for prev in estados) * emision[estado][obs[t]]
    return f

# Algoritmo Backward
def backward(obs):
    b = [{} for _ in range(len(obs))]
    for estado in estados:
        b[-1][estado] = 1

    for t in reversed(range(len(obs) - 1)):
        for estado in estados:
            b[t][estado] = sum(transicion[estado][siguiente] * emision[siguiente][obs[t+1]] * b[t+1][siguiente] for siguiente in estados)
    return b

# Combinar forward y backward
def forward_backward(obs):
    f = forward(obs)
    b = backward(obs)
    resultado = []

    for t in range(len(obs)):
        probs = {}
        total = 0
        for estado in estados:
            probs[estado] = f[t][estado] * b[t][estado]
            total += probs[estado]
        for estado in estados:
            probs[estado] /= total  # Normalizamos
        resultado.append(probs)
    return resultado

# Ejecutamos
resultado = forward_backward(observada)
for t, probs in enumerate(resultado):
    print(f" Tiempo {t+1} ({observada[t]}):")
    for estado, prob in probs.items():
        print(f"  - {estado}: {prob:.4f}")
