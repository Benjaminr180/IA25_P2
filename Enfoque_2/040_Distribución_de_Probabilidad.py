import random

# Definir una distribución de probabilidad discreta
# Suponemos un dado de 6 caras, pero con probabilidades no uniformes
distribucion_probabilidad = {
    1: 0.1,  # P(1) = 0.1
    2: 0.2,  # P(2) = 0.2
    3: 0.1,  # P(3) = 0.1
    4: 0.2,  # P(4) = 0.2
    5: 0.2,  # P(5) = 0.2
    6: 0.1   # P(6) = 0.1
}

# Usamos una tolerancia para verificar que las probabilidades sumen 1
tolerancia = 1e-6  # Tolerancia de 1e-6 para la comparación
if abs(sum(distribucion_probabilidad.values()) - 1) > tolerancia:
    print("Advertencia: Las probabilidades no suman exactamente 1.")
else:
    # Simulación: Lanzar el dado basado en la distribución dada
    def lanzar_dado(distribucion):
        caras = list(distribucion.keys())
        probabilidades = list(distribucion.values())
        return random.choices(caras, probabilidades)[0]

    # Lanzar el dado 10000 veces para simular la distribución
    resultados = [lanzar_dado(distribucion_probabilidad) for _ in range(10000)]

    # Calcular la esperanza matemática (valor esperado)
    esperanza = sum(valor * distribucion_probabilidad[valor] for valor in distribucion_probabilidad)

    # Calcular la varianza
    varianza = sum((valor - esperanza)**2 * distribucion_probabilidad[valor] for valor in distribucion_probabilidad)

    # Mostrar resultados
    print(" Distribución de Probabilidad")
    print(f"Distribución de probabilidad del dado: {distribucion_probabilidad}")
    print(f"\nResultado de los lanzamientos (10000 veces): {resultados[:30]}...")  # Muestra los primeros 30 lanzamientos

    print("\n Cálculos")
    print(f"Esperanza matemática (valor esperado): {esperanza:.2f}")
    print(f"Varianza: {varianza:.2f}")
