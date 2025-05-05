# Definimos las probabilidades individuales
P_A = 0.5  # Probabilidad de A
P_B_given_A = 0.7  # Probabilidad de B dado A
P_C_given_A_and_B = 0.8  # Probabilidad de C dado A y B

# Usamos la regla de la cadena para calcular la probabilidad conjunta P(A, B, C)
P_ABC = P_A * P_B_given_A * P_C_given_A_and_B

# Mostramos el resultado
print(f"La probabilidad conjunta P(A, B, C) es: {P_ABC}")
