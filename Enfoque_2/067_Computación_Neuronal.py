# Neurona artificial simple sin librerías externas

def relu(x):
    return max(0, x)

def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))

# Entrada a la neurona (puedes cambiar estos valores)
entradas = [1.5, -2.0]

# Pesos asociados a cada entrada
pesos = [0.7, -1.2]

# Sesgo (bias)
bias = 0.5

# Cálculo de la suma ponderada
suma_ponderada = sum(e * p for e, p in zip(entradas, pesos)) + bias

# Aplicamos la función de activación
salida = relu(suma_ponderada)  # Puedes usar sigmoid(suma_ponderada) también

# Resultado
print(f"Salida de la neurona: {salida:.4f}")
