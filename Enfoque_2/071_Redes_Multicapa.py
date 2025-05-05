import math

# Función sigmoide como activación
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la sigmoide (opcional para aprendizaje, aquí no lo usamos)
def derivada_sigmoide(x):
    sx = sigmoide(x)
    return sx * (1 - sx)

# Cálculo hacia adelante en una red multicapa
def red_multicapa(entrada):
    # Pesos para capa oculta (2 neuronas)
    pesos_entrada_oculta = [
        [0.5, -0.4],  # neurona 1
        [0.9, 0.1]    # neurona 2
    ]
    sesgos_oculta = [0.1, -0.3]

    # Salida de la capa oculta
    salida_oculta = []
    for i in range(2):  # 2 neuronas ocultas
        suma = sum(entrada[j] * pesos_entrada_oculta[i][j] for j in range(len(entrada))) + sesgos_oculta[i]
        salida_oculta.append(sigmoide(suma))

    # Pesos y sesgo para la neurona de salida
    pesos_oculta_salida = [0.7, -0.6]
    sesgo_salida = 0.2

    # Cálculo de salida final
    salida_final = sum(salida_oculta[i] * pesos_oculta_salida[i] for i in range(2)) + sesgo_salida
    salida_final = sigmoide(salida_final)

    return salida_final

# Ejemplo de entrada
entrada = [1.0, 0.5]
salida = red_multicapa(entrada)

print(f"Entrada: {entrada}")
print(f"Salida de la red multicapa: {salida}")
