import random

# Simulación del lanzamiento de un dado de 6 caras para ilustrar la incertidumbre
# En cada lanzamiento no podemos saber con certeza qué número saldrá

def lanzar_dado():
    return random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6

# Lanzamos el dado varias veces para observar la variabilidad del resultado
numero_lanzamientos = 10
resultados = []

for _ in range(numero_lanzamientos):
    resultado = lanzar_dado()
    resultados.append(resultado)

# Mostramos los resultados de los lanzamientos
print("Resultados de los lanzamientos del dado:")
print(resultados)

# Contamos cuántas veces salió cada número
conteo = {cara: resultados.count(cara) for cara in range(1, 7)}

print("\nFrecuencia de cada número:")
for cara, cantidad in conteo.items():
    print(f"El número {cara} salió {cantidad} veces")

# Calculamos la probabilidad estimada (frecuencia relativa)
print("\nProbabilidades estimadas:")
for cara, cantidad in conteo.items():
    probabilidad = cantidad / numero_lanzamientos
    print(f"Probabilidad aproximada de obtener {cara}: {probabilidad:.2f}")
