# Definimos la función de negación (¬p)
def negacion(p):
    return not p

# Definimos la conjunción lógica (p ∧ q)
def conjuncion(p, q):
    return p and q

# Definimos la disyunción lógica (p ∨ q)
def disyuncion(p, q):
    return p or q

# Definimos la implicación lógica (p → q)
def implicacion(p, q):
    return (not p) or q

# Definimos el bicondicional lógico (p ↔ q)
def bicondicional(p, q):
    return p == q

# Lista con todas las combinaciones posibles de valores para p y q (True o False)
valores = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

# Imprimimos el encabezado de la tabla de verdad
print("p\tq\t¬p\tp∧q\tp∨q\tp→q\tp↔q")

# Recorremos cada combinación de valores
for p, q in valores:
    # Imprimimos los resultados de aplicar las operaciones lógicas a p y q
    print(
        f"{p}\t{q}\t{negacion(p)}\t{conjuncion(p, q)}\t{disyuncion(p, q)}\t{implicacion(p, q)}\t{bicondicional(p, q)}"
    )
