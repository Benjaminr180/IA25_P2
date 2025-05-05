import random

# Estados y transiciones
estados = ['Soleado', 'Nublado', 'Lluvioso']
transiciones = {
    'Soleado': {'Soleado': 0.6, 'Nublado': 0.3, 'Lluvioso': 0.1},
    'Nublado': {'Soleado': 0.2, 'Nublado': 0.6, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.1, 'Nublado': 0.4, 'Lluvioso': 0.5}
}

# Simular observaciones (como si fueran sensores del clima)
def generar_observaciones(estado_inicial, pasos):
    estado = estado_inicial
    secuencia = [estado]
    for _ in range(pasos):
        estado = random.choices(
            list(transiciones[estado].keys()),
            list(transiciones[estado].values())
        )[0]
        secuencia.append(estado)
    return secuencia

# Filtrado: última observación conocida
def filtrado(observaciones):
    return observaciones[-1]

# Predicción: predecir estado después de N pasos
def prediccion(estado_actual, pasos):
    estado = estado_actual
    for _ in range(pasos):
        estado = random.choices(
            list(transiciones[estado].keys()),
            list(transiciones[estado].values())
        )[0]
    return estado

# Ejecutar ejemplo
observaciones = generar_observaciones("Soleado", 10)
print(" Observaciones del clima:", observaciones)

# Aplicamos filtrado
estado_filtrado = filtrado(observaciones)
print(f" Estado actual estimado (Filtrado): {estado_filtrado}")

# Aplicamos predicción
estado_futuro = prediccion(estado_filtrado, 3)
print(f" Estado estimado dentro de 3 días (Predicción): {estado_futuro}")
