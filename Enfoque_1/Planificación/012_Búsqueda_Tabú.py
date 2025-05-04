import random

# Función objetivo (en este caso, una simple parábola invertida)
def funcion_objetivo(x):
    return -(x**2) + 10  # Queremos maximizar esta función

# Función para generar un vecino "aleatorio"
def vecino_actual(x):
    # Generamos un vecino moviendo el valor de x un poco (en este caso, un paso pequeño)
    return x + random.uniform(-1, 1)

# Búsqueda Tabú
def busqueda_tabu(funcion_objetivo, estado_inicial, max_iteraciones, tamaño_lista_tabu):
    estado_actual = estado_inicial
    lista_tabu = []  # Inicializamos la lista tabú como vacía
    mejor_solucion = estado_actual
    mejor_valor = funcion_objetivo(estado_actual)
    
    for _ in range(max_iteraciones):
        # Generamos un vecino aleatorio
        vecino = vecino_actual(estado_actual)
        
        # Verificamos si el vecino está en la lista tabú
        if vecino not in lista_tabu:
            # Si no está en la lista tabú, evaluamos su función objetivo
            if funcion_objetivo(vecino) > mejor_valor:
                mejor_solucion = vecino
                mejor_valor = funcion_objetivo(vecino)
            
            # Actualizamos el estado actual
            estado_actual = vecino
            
            # Añadimos el nuevo estado a la lista tabú
            lista_tabu.append(estado_actual)
            
            # Si la lista tabú se llena, eliminamos el estado más antiguo
            if len(lista_tabu) > tamaño_lista_tabu:
                lista_tabu.pop(0)
    
    return mejor_solucion

#  Prueba con estado inicial = 3 
estado_inicial = 3
max_iteraciones = 100  # Número máximo de iteraciones
tamaño_lista_tabu = 10  # Tamaño de la lista tabú

resultado = busqueda_tabu(funcion_objetivo, estado_inicial, max_iteraciones, tamaño_lista_tabu)
print(f"El valor óptimo encontrado es: {resultado}")
