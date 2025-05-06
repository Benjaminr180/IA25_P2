def unificacion(p1, p2):
    if len(p1) != len(p2):
        return False
    sustitucion = {}
    for a, b in zip(p1, p2):
        if a == b:
            continue
        elif a.islower():
            sustitucion[a] = b
        elif b.islower():
            sustitucion[b] = a
        else:
            return False
    return sustitucion

# Ejemplo de uso
print(unificacion(["X", "gusta", "helado"], ["ana", "gusta", "helado"]))
