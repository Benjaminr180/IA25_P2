import random
import math

# Función objetivo (en este caso, una simple parábola invertida)
def funcion_objetivo(x):
    return -(x**2) + 10  # Queremos maximizar esta función

# Función para generar un vecino "aleatorio"
def vecino_actual(x):
    return x + random.uniform(-1, 1)  # Desplazamos el valor de x un poco

# Búsqueda de Temple Simulado
def temple_simulado(funcion_objetivo, estado_inicial, temperatura_inicial, tasa_enfriamiento, max_iteraciones):
    estado_actual = estado_inicial
    mejor_solucion = estado_actual
    mejor_valor = funcion_objetivo(estado_actual)
    
    temperatura = temperatura_inicial
    
    for iteracion in range(max_iteraciones):
        # Generamos un vecino aleatorio
        vecino = vecino_actual(estado_actual)
        
        # Calculamos las energías (valores de la función objetivo)
        energia_actual = funcion_objetivo(estado_actual)
        energia_vecino = funcion_objetivo(vecino)
        
        # Si el vecino es mejor, lo aceptamos
        if energia_vecino > energia_actual:
            estado_actual = vecino
            # Si encontramos una mejor solución, actualizamos la mejor solución
            if energia_vecino > mejor_valor:
                mejor_solucion = vecino
                mejor_valor = energia_vecino
        else:
            # Si el vecino es peor, lo aceptamos con una probabilidad
            probabilidad = math.exp((energia_vecino - energia_actual) / temperatura)
            if random.random() < probabilidad:
                estado_actual = vecino
        
        # Reducimos la temperatura
        temperatura *= tasa_enfriamiento
    
    return mejor_solucion

# --------- Prueba con estado inicial = 3 ---------
estado_inicial = 3
temperatura_inicial = 1000  # Temperatura inicial
tasa_enfriamiento = 0.99  # Tasa de enfriamiento
max_iteraciones = 100  # Número máximo de iteraciones

resultado = temple_simulado(funcion_objetivo, estado_inicial, temperatura_inicial, tasa_enfriamiento, max_iteraciones)
print(f"El valor óptimo encontrado es: {resultado}")
