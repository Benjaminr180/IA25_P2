import random

# Definir los estados posibles y las probabilidades de transición
estados = ['soleado', 'lluvioso']
transiciones = {
    'soleado': {'soleado': 0.8, 'lluvioso': 0.2},
    'lluvioso': {'soleado': 0.4, 'lluvioso': 0.6}
}

# Función para elegir el siguiente estado según la probabilidad
def siguiente_estado(estado_actual):
    return random.choices(
        population=estados, 
        weights=[transiciones[estado_actual]['soleado'], transiciones[estado_actual]['lluvioso']],
        k=1
    )[0]

# Simulamos el clima durante 10 días, comenzando con "soleado"
estado_inicial = 'soleado'
dias = 10

# Empezamos con el clima del primer día
estado_actual = estado_inicial
print(f"Día 1: El clima es {estado_actual}")

# Simulamos los siguientes días
for dia in range(2, dias + 1):
    estado_actual = siguiente_estado(estado_actual)
    print(f"Día {dia}: El clima es {estado_actual}")
