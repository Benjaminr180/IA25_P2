def diagnostico_temperatura(temperatura):
    if temperatura > 38:
        return "Fiebre detectada"
    elif temperatura < 35:
        return "Hipotermia detectada"
    else:
        return "Temperatura normal"

# Ejemplo de uso
print(diagnostico_temperatura(39))
