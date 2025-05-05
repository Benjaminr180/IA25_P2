import random

# Definimos una distribución de probabilidad simple para un dado
# Puedo pensar que el dado tiene 6 caras y queremos muestrear
# P(x) = Probabilidad de que salga un número x en el dado

# Probabilidad de que salga cada número (uniforme)
def distribucion_dado(x):
    if 1 <= x <= 6:
        return 1 / 6  # Probabilidad uniforme
    return 0

# Función de muestreo directo (muestra un valor de acuerdo con la distribución dada)
def muestreo_directo():
    # Generamos un número aleatorio entre 1 y 6
    return random.randint(1, 6)

# Función de muestreo por rechazo
def muestreo_por_rechazo():
    # Definimos la función de probabilidad máxima en el rango dado (en este caso 1/6)
    max_prob = 1 / 6  # En un dado, la probabilidad máxima es 1/6
    
    # Continuamos hasta obtener una muestra válida
    while True:
        # Muestreamos un número aleatorio
        candidato = random.randint(1, 6)
        u = random.random()  # Generamos un número aleatorio entre 0 y 1

        # Si el número aleatorio está debajo de la probabilidad de esa cara del dado, aceptamos el valor
        if u < distribucion_dado(candidato) / max_prob:
            return candidato

# Realizamos el muestreo directo y por rechazo
muestra_directa = [muestreo_directo() for _ in range(10)]
muestra_rechazo = [muestreo_por_rechazo() for _ in range(10)]

# Mostramos las muestras obtenidas
print("Muestreo directo (10 muestras):", muestra_directa)
print("Muestreo por rechazo (10 muestras):", muestra_rechazo)
