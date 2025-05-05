import random
from collections import Counter

# Simular lanzamientos de un dado de 6 caras
def lanzar_dado():
    return random.randint(1, 6)

numero_lanzamientos = 10000
resultados = [lanzar_dado() for _ in range(numero_lanzamientos)]

# Contar ocurrencias de cada cara
conteo = Counter(resultados)

# Evento A: salir un número par
# Evento B: salir un número mayor que 3 (4, 5 o 6)
caras_A = [2, 4, 6]
caras_B = [4, 5, 6]

# Probabilidad de B: P(B)
P_B = sum(conteo[c] for c in caras_B) / numero_lanzamientos

# Probabilidad conjunta A ∧ B: P(A y B)
P_AyB = sum(conteo[c] for c in caras_A if c in caras_B) / numero_lanzamientos

# Probabilidad condicionada P(A | B) = P(A ∧ B) / P(B)
P_A_cond_B = P_AyB / P_B

print("\n Probabilidad Condicionada")
print(f"Probabilidad de par dado que es >3: {P_A_cond_B:.4f}")

# Ahora, un ejemplo de normalización de puntajes no normalizados
puntajes = {
    'Estrategia X': 2.5,
    'Estrategia Y': 1.0,
    'Estrategia Z': 6.5
}

suma_puntajes = sum(puntajes.values())
# Normalizamos: probabilidad_i = puntaje_i / suma_total
probabilidades_normalizadas = {
    estrategia: puntaje / suma_puntajes
    for estrategia, puntaje in puntajes.items()
}

print("\n Probabilidades Normalizadas")
for estrategia, prob in probabilidades_normalizadas.items():
    print(f"{estrategia}: {prob:.4f}")
