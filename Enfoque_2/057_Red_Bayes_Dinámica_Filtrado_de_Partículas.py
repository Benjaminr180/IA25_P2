import random

# Configuración
num_particulas = 1000
estado_real = 20  # Valor real (que el filtro intenta encontrar)
ruido_medicion = 2

# Paso 1: Inicialización
particulas = [random.uniform(0, 40) for _ in range(num_particulas)]

def medir_estado(estado_real):
    return estado_real + random.uniform(-ruido_medicion, ruido_medicion)

def peso_particula(p, medida):
    return 1.0 / abs(p - medida + 0.1)  # +0.1 para evitar división por 0

# Simulación
for t in range(1, 6):
    medida = medir_estado(estado_real)

    # Paso 2 y 3: Predicción y actualización de pesos
    pesos = [peso_particula(p, medida) for p in particulas]

    # Paso 4: Remuestreo (selecciona mejores partículas)
    particulas = random.choices(particulas, weights=pesos, k=num_particulas)

    # Estimación promedio
    estimacion = sum(particulas) / num_particulas

    print(f" Tiempo {t}")
    print(f"  Medida observada: {medida:.2f}")
    print(f"  Estimación por partículas: {estimacion:.2f}")
    print()
