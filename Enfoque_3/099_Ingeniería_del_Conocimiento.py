base_de_conocimiento = {
    "es_mamifero": ["perro", "gato", "humano"],
    "tiene_pelo": ["perro", "gato"],
    "tiene_pulgares": ["humano"]
}

def consultar_hecho(categoria, elemento):
    return elemento in base_de_conocimiento.get(categoria, [])

# Ejemplo de uso
print(consultar_hecho("tiene_pulgares", "humano"))
