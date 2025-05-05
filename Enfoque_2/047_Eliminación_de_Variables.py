# Definimos las probabilidades condicionadas de las variables A y B
P_A = {
    True: 0.6,  # Probabilidad de que A sea True
    False: 0.4  # Probabilidad de que A sea False
}

P_B_given_A = {
    True: {True: 0.7, False: 0.3},  # Probabilidad de B dado A=True
    False: {True: 0.2, False: 0.8}  # Probabilidad de B dado A=False
}

# Eliminación de Variables: Calcular P(A) marginalizando sobre B
def eliminacion_variables(P_A, P_B_given_A):
    # Inicializamos la probabilidad marginal de A
    P_A_marginal = {True: 0, False: 0}
    
    # Sumamos sobre B para eliminar B y calcular P(A)
    for a in [True, False]:
        # La probabilidad marginal de A se obtiene sumando sobre todas las posibles
        # combinaciones de B (True o False)
        suma_probabilidades_B = P_B_given_A[a][True] + P_B_given_A[a][False]
        P_A_marginal[a] = P_A[a] * suma_probabilidades_B
    
    # Normalizamos la probabilidad para que sume 1 (probabilidad total)
    total_prob = P_A_marginal[True] + P_A_marginal[False]
    P_A_marginal = {k: v / total_prob for k, v in P_A_marginal.items()}
    
    return P_A_marginal

# Llamamos a la función y mostramos el resultado
P_A_resultado = eliminacion_variables(P_A, P_B_given_A)
print(f"Probabilidad marginal de A:\n{P_A_resultado}")
