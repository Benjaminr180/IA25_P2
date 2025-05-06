hechos = ["animal(leon)", "animal(tigre)"]
reglas = [("animal(X)", "carnivoro(X)")]

def aplicar_reglas_simples(hechos, reglas):
    nuevos = []
    for regla in reglas:
        ant, cons = regla
        if "X" in ant:
            for hecho in hechos:
                if hecho.startswith("animal("):
                    x = hecho[7:-1]
                    nuevo = cons.replace("X", x)
                    nuevos.append(nuevo)
    return nuevos

# Ejemplo de uso
print(aplicar_reglas_simples(hechos, reglas))
