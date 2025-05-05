# Datos previos (a priori)
P_gripe = 0.1               # Probabilidad de que alguien tenga gripe
P_no_gripe = 0.9            # Probabilidad de que no tenga gripe

# Verosimilitud
P_fiebre_dado_gripe = 0.8   # Si tiene gripe, 80% de probabilidad que tenga fiebre
P_fiebre_dado_no_gripe = 0.2 # Si no tiene gripe, 20% de probabilidad de fiebre

# Evidencia (normalización)
P_fiebre = (P_fiebre_dado_gripe * P_gripe) + (P_fiebre_dado_no_gripe * P_no_gripe)

# Aplicamos la regla de Bayes
P_gripe_dado_fiebre = (P_fiebre_dado_gripe * P_gripe) / P_fiebre
P_no_gripe_dado_fiebre = (P_fiebre_dado_no_gripe * P_no_gripe) / P_fiebre

# Mostrar resultados
print(" Diagnóstico basado en fiebre:")
print(f" Probabilidad de tener gripe: {P_gripe_dado_fiebre:.2f}")
print(f" Probabilidad de NO tener gripe: {P_no_gripe_dado_fiebre:.2f}")
