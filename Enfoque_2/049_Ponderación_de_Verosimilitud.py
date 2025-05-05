import random

# Función de verosimilitud para una distribución normal
def verosimilitud(mu, sigma, datos):
    """
    Calcula la verosimilitud de un conjunto de datos dado un modelo normal con media mu y desviación estándar sigma.
    """
    # Usamos la fórmula de la distribución normal
    from math import exp, sqrt, pi
    
    verosimilitud_total = 1
    for dato in datos:
        # Fórmula de la verosimilitud para cada dato en una distribución normal
        probabilidad_dato = (1 / (sqrt(2 * pi * sigma ** 2))) * exp(-(dato - mu) ** 2 / (2 * sigma ** 2))
        verosimilitud_total *= probabilidad_dato
    return verosimilitud_total

# Generar algunos datos de ejemplo (simulados con una media de 10 y desviación estándar de 2)
datos_simulados = [random.gauss(10, 2) for _ in range(100)]

# Modelos para los cuales vamos a evaluar la verosimilitud
modelos = [(10, 2), (12, 3), (8, 1)]

# Evaluamos la verosimilitud para cada modelo
resultados = []
for mu, sigma in modelos:
    verosimilitud_modelo = verosimilitud(mu, sigma, datos_simulados)
    resultados.append((mu, sigma, verosimilitud_modelo))

# Ordenamos los modelos por su verosimilitud (de mayor a menor)
resultados_ordenados = sorted(resultados, key=lambda x: x[2], reverse=True)

# Mostramos los modelos con sus verosimilitudes
print("Modelos evaluados y sus verosimilitudes:")
for modelo in resultados_ordenados:
    print(f"Modelo: Media={modelo[0]}, Desviación Estándar={modelo[1]}, Verosimilitud={modelo[2]:.5f}")
