# Verificamos si dos proposiciones son equivalentes mediante tablas de verdad

def tabla_verdad_equivalencia(exp1, exp2):
    print(f"Expresión 1: {exp1}, Expresión 2: {exp2}")
    print("A | B | Exp1 | Exp2 | ¿Iguales?")
    for A in [True, False]:
        for B in [True, False]:
            val1 = eval(exp1.replace('A', str(A)).replace('B', str(B)))
            val2 = eval(exp2.replace('A', str(A)).replace('B', str(B)))
            iguales = val1 == val2
            print(f"{int(A)} | {int(B)} |  {int(val1)}   |  {int(val2)}   |    {iguales}")

tabla_verdad_equivalencia("A and B", "not (not A or not B)")  # Ley de De Morgan
