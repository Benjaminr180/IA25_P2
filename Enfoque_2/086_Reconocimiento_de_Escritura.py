# Simulamos un conjunto simple de caracteres escritos a mano
escritura = {
    '1': ['   #', '  ##', '   #', '   #', '   #'],
    '2': ['###', '   #', '###', '#   ', '###']
}

# Función para mostrar la escritura
def reconocer_escritura(digito):
    if digito in escritura:
        for linea in escritura[digito]:
            print(linea)

# Mostrar el "reconocimiento" de un dígito
reconocer_escritura('1')
