def escalon(x):
    return 1 if x >= 0 else 0

def perceptron(inputs, pesos, bias):
    suma = sum(i * w for i, w in zip(inputs, pesos)) + bias
    return escalon(suma)

def adaline(inputs, pesos, bias, tasa_aprendizaje=0.1):
    salida = sum(i * w for i, w in zip(inputs, pesos)) + bias
    return salida  # No se aplica escalón, salida es continua

def madaline(entradas, pesos_m1, pesos_m2, bias_m1, bias_m2, bias_salida):
    salida_m1 = escalon(sum(i * w for i, w in zip(entradas, pesos_m1)) + bias_m1)
    salida_m2 = escalon(sum(i * w for i, w in zip(entradas, pesos_m2)) + bias_m2)
    salida_final = escalon(salida_m1 * 1 + salida_m2 * 1 + bias_salida)
    return salida_final

# Ejemplo de prueba
entradas = [1, 0]
pesos = [0.5, -0.5]
bias = 0.1

print("PERCEPTRÓN")
print("Entrada:", entradas)
print("Salida:", perceptron(entradas, pesos, bias))

print("\nADALINE")
print("Entrada:", entradas)
print("Salida:", round(adaline(entradas, pesos, bias), 2))

print("\nMADALINE")
pesos_m1 = [0.6, -0.4]
pesos_m2 = [0.3, 0.7]
bias_m1 = -0.2
bias_m2 = 0.1
bias_salida = -0.5

print("Entrada:", entradas)
print("Salida:", madaline(entradas, pesos_m1, pesos_m2, bias_m1, bias_m2, bias_salida))
