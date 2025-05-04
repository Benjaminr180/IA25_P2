import random

# Función de aptitud (fitness): mide qué tan buena es una solución
# En este caso, queremos que la suma de los genes sea igual a 10
def funcion_aptitud(individuo):
    return abs(10 - sum(individuo))  # Queremos acercarnos a 10

# Generar población inicial con cromosomas aleatorios
# Cada individuo tiene 'longitud' genes (0 o 1)
def generar_poblacion(tamano, longitud):
    poblacion = []
    for _ in range(tamano):
        individuo = [random.randint(0, 1) for _ in range(longitud)]  # Cromosoma aleatorio
        poblacion.append(individuo)
    return poblacion

# Selección por torneo: elige dos individuos aleatorios y selecciona el de mejor aptitud
def seleccion(poblacion):
    seleccionados = random.sample(poblacion, 2)  # Selecciona dos individuos aleatorios
    seleccionados.sort(key=lambda x: funcion_aptitud(x))  # Ordena por aptitud (menor es mejor)
    return seleccionados[0]  # Retorna el mejor individuo

# Cruzamiento (crossover): crea dos nuevos individuos combinando los genes de dos padres
def cruzamiento(individuo1, individuo2):
    punto_cruce = random.randint(1, len(individuo1) - 1)  # El punto de corte para el cruce
    hijo1 = individuo1[:punto_cruce] + individuo2[punto_cruce:]  # Combina los genes
    hijo2 = individuo2[:punto_cruce] + individuo1[punto_cruce:]  # Lo mismo para el otro hijo
    return hijo1, hijo2  # Retorna los dos hijos

# Mutación: introduce un cambio aleatorio en el cromosoma con una probabilidad
def mutacion(individuo, probabilidad):
    for i in range(len(individuo)):
        if random.random() < probabilidad:  # Si pasa la probabilidad de mutación
            individuo[i] = 1 - individuo[i]  # Cambia el valor del gen (de 0 a 1 o de 1 a 0)
    return individuo  # Retorna el cromosoma mutado

# Algoritmo Genético: ejecución del proceso de selección, cruzamiento, mutación y reemplazo
def algoritmo_genetico(tamano_poblacion, longitud_cromosoma, generaciones, probabilidad_mutacion):
    # Se genera una población inicial aleatoria
    poblacion = generar_poblacion(tamano_poblacion, longitud_cromosoma)
    
    # Se ejecuta por un número de generaciones
    for generacion in range(generaciones):
        poblacion.sort(key=lambda x: funcion_aptitud(x))  # Ordena por aptitud
        mejor_individuo = poblacion[0]  # El mejor individuo de la población
        print(f"Generación {generacion+1}: Mejor aptitud = {funcion_aptitud(mejor_individuo)}")
        
        if funcion_aptitud(mejor_individuo) == 0:  # Si encontramos la solución perfecta
            break  # Termina el algoritmo si encontramos la solución perfecta
        
        # Crear nueva población
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = seleccion(poblacion)  # Selecciona un padre
            padre2 = seleccion(poblacion)  # Selecciona el otro padre
            hijo1, hijo2 = cruzamiento(padre1, padre2)  # Cruza los padres para crear dos hijos
            nueva_poblacion.append(mutacion(hijo1, probabilidad_mutacion))  # Aplica mutación en el hijo1
            nueva_poblacion.append(mutacion(hijo2, probabilidad_mutacion))  # Aplica mutación en el hijo2
        
        poblacion = nueva_poblacion  # La nueva población reemplaza la antigua
    
    return poblacion[0]  # Retorna el mejor individuo encontrado

# Ejecución del algoritmo
tamano_poblacion = 10  # Tamaño de la población
longitud_cromosoma = 5  # Número de genes por cromosoma
generaciones = 20  # Número de generaciones a ejecutar
probabilidad_mutacion = 0.1  # Probabilidad de mutación

# Ejecutamos el algoritmo genético y obtenemos la solución
solucion = algoritmo_genetico(tamano_poblacion, longitud_cromosoma, generaciones, probabilidad_mutacion)
print("Solución encontrada:", solucion)
