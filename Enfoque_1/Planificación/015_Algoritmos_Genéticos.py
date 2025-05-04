import random

# Función objetivo (en este caso, la parabólica invertida)
def funcion_objetivo(x):
    return -(x**2) + 10

# Generar población inicial aleatoria
def generar_poblacion(tamano_poblacion, longitud_cromosoma):
    poblacion = []
    for _ in range(tamano_poblacion):
        cromosoma = ''.join(random.choice('01') for _ in range(longitud_cromosoma))  # Cromosomas en binario
        poblacion.append(cromosoma)
    return poblacion

# Convertir cromosoma binario a valor decimal
def binario_a_decimal(cromosoma):
    return int(cromosoma, 2)  # Convierte de binario a decimal

# Función de aptitud: evalúa la calidad de la solución
def aptitud(cromosoma):
    x = binario_a_decimal(cromosoma)  # Convertimos el cromosoma a valor decimal
    return funcion_objetivo(x)

# Selección por torneo
def seleccion(poblacion):
    torneo = random.sample(poblacion, 2)  # Elegir 2 individuos al azar
    torneo.sort(key=lambda cromosoma: aptitud(cromosoma), reverse=True)  # Ordenamos por aptitud
    return torneo[0]  # Retornamos el mejor

# Cruzamiento (Crossover) de un punto
def crossover(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_corte] + padre2[punto_corte:]
    hijo2 = padre2[:punto_corte] + padre1[punto_corte:]
    return hijo1, hijo2

# Mutación: cambian un bit aleatorio
def mutacion(cromosoma, probabilidad_mutacion):
    cromosoma = list(cromosoma)
    for i in range(len(cromosoma)):
        if random.random() < probabilidad_mutacion:  # Probabilidad de mutación
            cromosoma[i] = '1' if cromosoma[i] == '0' else '0'  # Cambiar el bit
    return ''.join(cromosoma)

# Algoritmo Genético
def algoritmo_genetico(tamano_poblacion, longitud_cromosoma, generacion_maxima, probabilidad_mutacion):
    poblacion = generar_poblacion(tamano_poblacion, longitud_cromosoma)
    
    for generacion in range(generacion_maxima):
        nueva_poblacion = []
        
        # Selección y reproducción (crossover)
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo1, hijo2 = crossover(padre1, padre2)
            
            # Mutación de los hijos
            hijo1 = mutacion(hijo1, probabilidad_mutacion)
            hijo2 = mutacion(hijo2, probabilidad_mutacion)
            
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
        
        # Reemplazo de la población
        poblacion = nueva_poblacion[:tamano_poblacion]  # Aseguramos que la población no crezca
    
    # Buscamos el mejor individuo
    mejor_individuo = max(poblacion, key=lambda cromosoma: aptitud(cromosoma))
    mejor_valor = aptitud(mejor_individuo)
    return mejor_individuo, mejor_valor

# ----------- Ejecución -----------

tamano_poblacion = 10  # Número de individuos en la población
longitud_cromosoma = 10  # Longitud de cada cromosoma (número de bits)
generacion_maxima = 100  # Número máximo de generaciones
probabilidad_mutacion = 0.01  # Probabilidad de que un bit se muta

mejor_individuo, mejor_valor = algoritmo_genetico(tamano_poblacion, longitud_cromosoma, generacion_maxima, probabilidad_mutacion)
print(f"Mejor individuo encontrado: {mejor_individuo} con valor de aptitud: {mejor_valor}")
