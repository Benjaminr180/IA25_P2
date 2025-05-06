def encadenamiento_adelante(hechos, reglas):
    nuevos = hechos[:]
    while True:
        agregado = False
        for antecedente, consecuente in reglas:
            if antecedente in nuevos and consecuente not in nuevos:
                nuevos.append(consecuente)
                agregado = True
        if not agregado:
            break
    return nuevos

# Ejemplo de uso
hechos = ["llueve"]
reglas = [("llueve", "mojado")]
print(encadenamiento_adelante(hechos, reglas))
def encadenamiento_atras(hechos, reglas, objetivo):
    if objetivo in hechos:
        return True
    for antecedente, consecuente in reglas:
        if consecuente == objetivo:
            if encadenamiento_atras(hechos, reglas, antecedente):
                return True
    return False

# Ejemplo de uso
hechos = ["llueve"]
reglas = [("llueve", "mojado")]
print(encadenamiento_atras(hechos, reglas, "mojado"))
