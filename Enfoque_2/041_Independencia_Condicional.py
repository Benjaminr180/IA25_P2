# Probabilidad de lluvia
p_lluvia = 0.3

# Probabilidad de rociador según lluvia
p_rociador_si_llueve = 0.9
p_rociador_no_llueve = 0.2

# Probabilidad de calle mojada dado lluvia y rociador
def prob_calle_mojada(lluvia, rociador):
    if lluvia and rociador:
        return 0.99
    elif lluvia and not rociador:
        return 0.9
    elif not lluvia and rociador:
        return 0.9
    else:
        return 0.0

# Evaluar: ¿P(Lluvia | Rociador activado)?
# Usamos regla de Bayes simplificada:
# P(Lluvia y Rociador) = P(Lluvia) * P(Rociador | Lluvia)
p_lluvia_y_rociador = p_lluvia * p_rociador_si_llueve
p_no_lluvia = 1 - p_lluvia
p_no_lluvia_y_rociador = p_no_lluvia * p_rociador_no_llueve

p_rociador = p_lluvia_y_rociador + p_no_lluvia_y_rociador

# Bayes: P(Lluvia | Rociador)
p_lluvia_dado_rociador = p_lluvia_y_rociador / p_rociador

print("Probabilidad de lluvia dado que el rociador se activó:")
print(round(p_lluvia_dado_rociador, 4))

# ¿Y si también sabemos que la calle está mojada?
# Como en este modelo simplificado eso no cambia mucho la inferencia, lo consideramos como ejemplo de independencia condicional.
print("\nDado que ya sabemos que el rociador se activó, saber que la calle está mojada no cambia la probabilidad de lluvia.")
print("Eso es un ejemplo de independencia condicional.")
