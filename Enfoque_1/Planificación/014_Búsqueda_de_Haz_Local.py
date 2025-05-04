import random

# Función objetivo (en este caso, una simple parábola invertida)
def funcion_objetivo(x):
    return -(x**2) + 10  # Queremos maximizar esta función

# Función para generar un vecino "aleatorio"
def vecino_actual(x):
    return x + random.uniform(-1, 1)  # Desplazamos el valor de x un poco

# Búsqueda de Haz Local
def busqueda_haz_local(funcion_objetivo, estado_iniciales, k, max_iteraciones):
    estados = estado_iniciales  # Lista de estados iniciales (haz)
    
    for iteracion in range(max_iteraciones):
        vecinos = []
        
        # Generamos los vecinos de todos los estados en el haz
        for estado in estados:
            vecino = vecino_actual(estado)
            vecinos.append((vecino, funcion_objetivo(vecino)))
        
        # Ordenamos los vecinos por el valor de la función objetivo (de mayor a menor)
        vecinos.sort(key=lambda x: x[1], reverse=True)
        
        # Seleccionamos las k mejores soluciones
        estados = [vecino[0] for vecino in vecinos[:k]]
    
    # Devolvemos el mejor estado encontrado
    mejor_estado = max(estados, key=funcion_objetivo)
    return mejor_estado

# --------- Prueba con un haz de 3 estados iniciales ---------
estado_iniciales = [3, 5, 7]  # Tres soluciones iniciales aleatorias
k = 3  # Tamaño del haz (número de soluciones a mantener)
max_iteraciones = 100  # Número máximo de iteraciones

resultado = busqueda_haz_local(funcion_objetivo, estado_iniciales, k, max_iteraciones)
print(f"El valor óptimo encontrado es: {resultado}")
