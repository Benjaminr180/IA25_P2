import random

# Datos con etiquetas desconocidas (simulados)
datos = [1.1, 1.9, 1.8, 5.0, 6.2, 5.8]

# Inicialización de parámetros
media_A = 2.0
media_B = 5.0
varianza = 1.0

def gauss(x, mu, var):
    import math
    return (1 / ((2 * math.pi * var) ** 0.5)) * math.exp(-(x - mu) ** 2 / (2 * var))

# Iteraciones del algoritmo EM
for paso in range(5):
    responsabilidades = []
    for x in datos:
        prob_A = gauss(x, media_A, varianza)
        prob_B = gauss(x, media_B, varianza)
        total = prob_A + prob_B
        responsabilidades.append((prob_A / total, prob_B / total))  # E-step

    # M-step: actualizar medias
    suma_A = sum(r[0] * x for r, x in zip(responsabilidades, datos))
    suma_B = sum(r[1] * x for r, x in zip(responsabilidades, datos))
    total_A = sum(r[0] for r in responsabilidades)
    total_B = sum(r[1] for r in responsabilidades)
    
    media_A = suma_A / total_A
    media_B = suma_B / total_B

    print(f" Iteración {paso + 1}")
    print(f"Media estimada A: {media_A:.2f}")
    print(f"Media estimada B: {media_B:.2f}")
    print("-" * 30)
