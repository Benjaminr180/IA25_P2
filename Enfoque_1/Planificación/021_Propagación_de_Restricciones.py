# Función para propagar restricciones
def propagacion_restricciones(variables, dominios, restricciones):
    """
    Propaga las restricciones sobre las variables eliminando valores de sus dominios
    que no son válidos debido a las restricciones.
    """
    # Mientras haya alguna variable que tenga valores posibles
    cambios = True
    while cambios:
        cambios = False
        for variable in variables:
            for valor in list(dominios[variable]):
                valido = True
                # Revisa todas las restricciones de la variable
                for restriccion in restricciones:
                    if restriccion[0] == variable and valor == dominios[restriccion[1]][0]:
                        valido = False
                        break
                # Si el valor no es válido, lo eliminamos del dominio de la variable
                if not valido:
                    dominios[variable].remove(valor)
                    cambios = True
    return dominios

# Variables con sus dominios de valores
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Restricciones que dicen que A no puede ser igual a B, y B no puede ser igual a C
restricciones = [('A', 'B'), ('B', 'C')]

# Aplicamos la propagación de restricciones
dominios_reducidos = propagacion_restricciones(variables, dominios, restricciones)

# Imprimimos los dominios después de la propagación
print("Dominios reducidos después de la propagación de restricciones:", dominios_reducidos)
