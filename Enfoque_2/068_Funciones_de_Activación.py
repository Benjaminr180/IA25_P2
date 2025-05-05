import math

# Entrada de ejemplo
x = float(input("Ingresa un valor para x: "))

# Funciones de activación
def step(x):
    return 1 if x >= 0 else 0

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def tanh(x):
    return math.tanh(x)

def relu(x):
    return max(0, x)

def leaky_relu(x):
    return x if x > 0 else 0.01 * x

# Mostrar resultados
print("\nResultados de las funciones de activación:")
print(f"Step       : {step(x)}")
print(f"Sigmoid    : {sigmoid(x):.4f}")
print(f"Tanh       : {tanh(x):.4f}")
print(f"ReLU       : {relu(x):.4f}")
print(f"Leaky ReLU : {leaky_relu(x):.4f}")
