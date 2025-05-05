# Usamos el mismo principio anterior para hacer inferencias
# La inferencia básica es encadenar reglas hasta obtener la conclusión deseada
# Creamos una base de conocimiento simple como una lista de proposiciones
base_conocimiento = [
    "A => B",  # Si A entonces B
    "B => C",  # Si B entonces C
    "A"        # A es verdadero
]

# Función para evaluar si una proposición es verdadera usando la base de conocimiento
def evaluar_bc(bc, proposicion):
    hechos = set()
    for regla in bc:
        if "=>" not in regla:
            hechos.add(regla)
    
    cambiando = True
    while cambiando:
        cambiando = False
        for regla in bc:
            if "=>" in regla:
                antecedente, consecuente = regla.split("=>")
                antecedente = antecedente.strip()
                consecuente = consecuente.strip()
                if antecedente in hechos and consecuente not in hechos:
                    hechos.add(consecuente)
                    cambiando = True

    return proposicion in hechos

# Verificamos si C se deduce
print("¿Se puede deducir C?:", evaluar_bc(base_conocimiento, "C"))
def inferir(base, objetivo):
    return evaluar_bc(base, objetivo)

# Prueba con otra proposición
print("¿Se puede inferir B?:", inferir(base_conocimiento, "B"))
