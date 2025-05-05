# Probabilidades base
prob_lluvia = 0.2  # P(Lluvia)
prob_rociador = {
    True: 0.01,     # P(Rociador | Lluvia)
    False: 0.4
}
prob_cesped_mojado = {
    (True, True): 0.99,   # P(Mojado | Lluvia, Rociador)
    (True, False): 0.9,
    (False, True): 0.9,
    (False, False): 0.0
}

# Calcular probabilidad conjunta para cada combinación
from itertools import product

print("\nAnálisis de Red Bayesiana: Lluvia, Rociador, Césped Mojado\n")

for lluvia, rociador in product([True, False], repeat=2):
    p_lluvia = prob_lluvia if lluvia else 1 - prob_lluvia
    p_rociador = prob_rociador[lluvia] if rociador else 1 - prob_rociador[lluvia]
    p_mojado = prob_cesped_mojado[(lluvia, rociador)]

    # Probabilidad conjunta
    p_total = p_lluvia * p_rociador * p_mojado

    print(f"Lluvia: {lluvia}, Rociador: {rociador}, Césped mojado: {p_mojado:.2f} → P = {p_total:.4f}")
