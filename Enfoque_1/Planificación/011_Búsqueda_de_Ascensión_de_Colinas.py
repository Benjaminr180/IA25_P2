import random

# Función objetivo (en este caso, una simple parábola invertida)
def funcion_objetivo(x):
    return -(x**2) + 10  # Queremos maximizar esta función

# Función para generar un vecino "aleatorio"
def vecino_actual(x):
    # Generamos un vecino moviendo el valor de x un poco (en este caso, un paso pequeño)
    return x + random.uniform(-1, 1)

# Búsqueda de Ascensión de Colinas
def ascension_de_colinas(funcion_objetivo, estado_inicial):
    estado_actual = estado_inicial
    while True:
        # Generamos un vecino aleatorio
        vecino = vecino_actual(estado_actual)
        
        # Evaluamos la función objetivo para el vecino y el estado actual
        if funcion_objetivo(vecino) > funcion_objetivo(estado_actual):
            # Si el vecino tiene un valor mejor, avanzamos hacia él
            estado_actual = vecino
        else:
            # Si no hay mejora, terminamos
            break
    
    return estado_actual

#  Prueba con estado inicial = 3 
estado_inicial = 5
resultado = ascension_de_colinas(funcion_objetivo, estado_inicial)
print(f"El valor óptimo encontrado es: {resultado}")
