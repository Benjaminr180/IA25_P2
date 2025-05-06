def agente_logico(percepcion):
    if percepcion == "obstaculo":
        return "gira_derecha"
    elif percepcion == "meta":
        return "avanza"
    else:
        return "explora"

# Ejemplo de uso
print(agente_logico("meta"))
