import re

# Simulamos un conjunto de texto
texto = """
Juan Pérez fue a la ciudad de Madrid y conoció a María García. Juntos viajaron a Barcelona.
"""

# Función para extraer entidades (por ejemplo, nombres propios)
def extraer_entidades(texto):
    # Utilizamos una expresión regular para buscar palabras que empiecen con mayúscula
    entidades = re.findall(r'\b[A-Z][a-z]*\b', texto)
    return entidades

# Extraer las entidades
entidades_extraidas = extraer_entidades(texto)

# Mostrar las entidades encontradas
print("Entidades extraídas:", entidades_extraidas)
