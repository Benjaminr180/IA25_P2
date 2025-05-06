# Simularemos el dominio con una lista de elementos (por ejemplo, personas con una edad)
dominio = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Sofía", "edad": 18},
    {"nombre": "Carlos", "edad": 25}
]

# Función que representa el predicado "es mayor de edad"
def es_mayor_de_edad(persona):
    return persona["edad"] >= 18

# Cuantificador universal (∀): ¿Todos son mayores de edad?
def para_todo(predicado, elementos):
    for e in elementos:
        if not predicado(e):
            return False
    return True

# Cuantificador existencial (∃): ¿Existe al menos uno mayor de edad?
def existe(predicado, elementos):
    for e in elementos:
        if predicado(e):
            return True
    return False

# Pruebas
print("¿Todos son mayores de edad? →", para_todo(es_mayor_de_edad, dominio))  # True
print("¿Existe alguien mayor de edad? →", existe(es_mayor_de_edad, dominio))  # True
