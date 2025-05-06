def skolemizar(sentencia):
    return sentencia.replace("∃x", "f(a)").replace("∀x", "")

# Ejemplo de uso
print(skolemizar("∀x ∃x ama(x, madre(x))"))
