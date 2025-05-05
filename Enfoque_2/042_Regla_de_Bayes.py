# Paso 1: Se definen las probabilidades iniciales conocidas del problema
p_enfermedad = 0.01               # Probabilidad previa de tener la enfermedad (muy baja, solo el 1%)
p_no_enfermedad = 1 - p_enfermedad  # Probabilidad de no tener la enfermedad

# Paso 2: Se definen las características de la prueba médica
p_positivo_si_enfermo = 0.99      # La prueba da positivo correctamente en el 99% de los casos con enfermedad
p_positivo_si_sano = 0.05         # La prueba da un falso positivo en el 5% de los casos sin enfermedad

# Paso 3: Se calcula la probabilidad total de obtener un resultado positivo en la prueba
# Esto incluye tanto los verdaderos positivos como los falsos positivos
p_positivo = (p_positivo_si_enfermo * p_enfermedad) + \
             (p_positivo_si_sano * p_no_enfermedad)

# Paso 4: Se aplica la Regla de Bayes para calcular la probabilidad de estar enfermo dado un resultado positivo
p_enfermo_dado_positivo = (p_positivo_si_enfermo * p_enfermedad) / p_positivo

# Paso 5: Se muestra el resultado final al usuario
print("Probabilidad de tener la enfermedad si la prueba dio positivo:")
print(round(p_enfermo_dado_positivo, 4))  # El resultado se redondea a 4 decimales
