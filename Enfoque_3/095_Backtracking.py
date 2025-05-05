# Problema de backtracking para encontrar asignación válida de variables
variables = ["X", "Y"]
dominios = {"X": [True, False], "Y": [True, False]}

def cumple_restriccion(asignacion):
    # Ejemplo: X => Y equivale a "no (X = True y Y = False)"
    return not (asignacion["X"] and not asignacion["Y"])

def backtracking(asignacion):
    if len(asignacion) == len(variables):
        if cumple_restriccion(asignacion):
            return asignacion
        return None

    var = next(v for v in variables if v not in asignacion)
    for valor in dominios[var]:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[var] = valor
        resultado = backtracking(nueva_asignacion)
        if resultado:
            return resultado
    return None

resultado = backtracking({})
print("Solución encontrada por backtracking:", resultado)
