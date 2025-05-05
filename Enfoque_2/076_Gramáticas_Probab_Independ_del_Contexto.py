import random

# Definimos una gramática probabilística simple
gramatica = {
    'S': [('NP', 'VP', 0.5), ('NP', 'VP', 'PP', 0.5)],  # S -> NP VP | NP VP PP
    'NP': [('Det', 'N', 0.5), ('Det', 'Adj', 'N', 0.5)],  # NP -> Det N | Det Adj N
    'VP': [('V', 'NP', 0.7), ('V', 'NP', 'PP', 0.3)],     # VP -> V NP | V NP PP
    'PP': [('P', 'NP', 1.0)],                             # PP -> P NP
    'Det': [('el', 0.5), ('la', 0.5)],                    # Det -> el | la
    'N': [('perro', 0.3), ('gato', 0.3), ('pelota', 0.2), ('niño', 0.2)],  # N -> perro | gato | pelota | niño
    'V': [('corre', 0.6), ('mira', 0.4)],                # V -> corre | mira
    'Adj': [('grande', 0.5), ('pequeño', 0.5)],          # Adj -> grande | pequeño
    'P': [('con', 1.0)]                                  # P -> con
}

# Función para seleccionar una producción según la probabilidad
def seleccionar_produccion(simbolo):
    producciones = gramatica[simbolo]
    # Aseguramos que las probabilidades estén como flotantes
    producciones = [(prod[0], float(prod[2])) if len(prod) == 3 else (prod[0], 1.0) for prod in producciones]
    # Seleccionamos una producción aleatoria según las probabilidades
    return random.choices([prod[0] for prod in producciones], weights=[prod[1] for prod in producciones])[0]

# Función recursiva para generar una frase
def generar_frase(simbolo):
    if simbolo not in gramatica:
        return simbolo  # Si es un símbolo terminal, lo devolvemos como palabra
    else:
        produccion = seleccionar_produccion(simbolo)
        frase = []
        for sub_simbolo in produccion:
            frase.append(generar_frase(sub_simbolo))
        return " ".join(frase)

# Generar una frase empezando por 'S'
frase_generada = generar_frase('S')
print("Frase generada aleatoriamente:")
print(frase_generada)
