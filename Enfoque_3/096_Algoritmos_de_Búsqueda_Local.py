import random

# Fórmula en forma normal conjuntiva (FNC)
fnc = [["A", "¬B"], ["B", "C"], ["¬A", "¬C"]]  # (A ∨ ¬B) ∧ (B ∨ C) ∧ (¬A ∨ ¬C)

def evaluar_clausula(clausula, asignacion):
    for literal in clausula:
        if literal.startswith("¬"):
            var = literal[1:]
            if not asignacion.get(var, False):
                return True
        else:
            if asignacion.get(literal, False):
                return True
    return False

def satisface_formula(fnc, asignacion):
    return all(evaluar_clausula(clausula, asignacion) for clausula in fnc)

def busqueda_local(fnc, max_intentos=100):
    variables = {lit.strip("¬") for clausula in fnc for lit in clausula}
    asignacion = {var: random.choice([True, False]) for var in variables}

    for _ in range(max_intentos):
        if satisface_formula(fnc, asignacion):
            return asignacion

        clausulas_falsas = [c for c in fnc if not evaluar_clausula(c, asignacion)]
        if not clausulas_falsas:
            return asignacion

        clausula = random.choice(clausulas_falsas)
        literal = random.choice(clausula)
        var = literal.strip("¬")
        asignacion[var] = not asignacion[var]  # Volteamos el valor

    return None

resultado = busqueda_local(fnc)
print("Solución encontrada por búsqueda local:", resultado)
