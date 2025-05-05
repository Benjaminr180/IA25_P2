# Probabilidades de clima
P_clima = {
    'soleado': 0.7,  # 70% de probabilidad de que esté soleado
    'lluvioso': 0.3  # 30% de probabilidad de que esté lluvioso
}

# Probabilidades condicionadas de llevar paraguas
P_paraguas_dado_clima = {
    'soleado': 0.1,   # 10% de probabilidad de llevar paraguas si está soleado
    'lluvioso': 0.9   # 90% de probabilidad de llevar paraguas si está lluvioso
}

# Inferencia por enumeración: Calcular la probabilidad de llevar paraguas (P(paraguas))
def inferencia_por_enumeracion(P_clima, P_paraguas_dado_clima):
    # Inicializamos la probabilidad de llevar paraguas
    probabilidad_paraguas = 0
    
    # Enumeramos sobre las posibilidades de clima (soleado y lluvioso)
    for clima, prob_clima in P_clima.items():
        # Calculamos la probabilidad conjunta P(clima y paraguas)
        probabilidad_paraguas += P_paraguas_dado_clima[clima] * prob_clima
    
    return probabilidad_paraguas

# Llamamos a la función y mostramos el resultado
probabilidad_paraguas = inferencia_por_enumeracion(P_clima, P_paraguas_dado_clima)
print(f"La probabilidad de llevar paraguas es: {probabilidad_paraguas:.2f}")
