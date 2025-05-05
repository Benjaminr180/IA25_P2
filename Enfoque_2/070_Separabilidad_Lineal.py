def es_linealmente_separable(puntos_clase1, puntos_clase2):
    """
    Verifica si hay una línea (en 2D) que puede separar los puntos de ambas clases.
    Esto lo haremos de forma visual, sin graficar, comparando las medias.
    """
    # Obtenemos promedios para estimar una línea divisoria
    media1_x = sum(p[0] for p in puntos_clase1) / len(puntos_clase1)
    media1_y = sum(p[1] for p in puntos_clase1) / len(puntos_clase1)

    media2_x = sum(p[0] for p in puntos_clase2) / len(puntos_clase2)
    media2_y = sum(p[1] for p in puntos_clase2) / len(puntos_clase2)

    # Vector de dirección entre medias (normal del posible hiperplano)
    direccion_x = media2_x - media1_x
    direccion_y = media2_y - media1_y

    # Verificamos en qué lado cae cada punto respecto a la línea
    def lado(p):
        return (p[0] - media1_x) * direccion_x + (p[1] - media1_y) * direccion_y

    lados_clase1 = [lado(p) for p in puntos_clase1]
    lados_clase2 = [lado(p) for p in puntos_clase2]

    # Si todos los productos tienen mismo signo, están separados
    if all(l < 0 for l in lados_clase1) and all(l > 0 for l in lados_clase2):
        return True
    if all(l > 0 for l in lados_clase1) and all(l < 0 for l in lados_clase2):
        return True
    return False

# Prueba con datos linealmente separables
clase1 = [(1, 2), (2, 3), (1, 3)]
clase2 = [(5, 6), (6, 5), (7, 7)]

print("¿Son separables linealmente?", es_linealmente_separable(clase1, clase2))
