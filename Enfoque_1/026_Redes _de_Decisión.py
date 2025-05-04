# Este código representa una Red de Decisión simple, donde se calculan utilidades esperadas
# para diferentes decisiones bajo incertidumbre.

# Diccionario que representa decisiones posibles con sus probabilidades y utilidades
decisiones = {
    "ir al parque": {
        "probabilidades": [0.6, 0.4],  # Probabilidad de sol y lluvia
        "utilidades": [10, 2]          # Utilidad si hay sol y si llueve
    },
    "quedarse en casa": {
        "probabilidades": [0.6, 0.4],
        "utilidades": [5, 5]
    },
    "ir al cine": {
        "probabilidades": [0.6, 0.4],
        "utilidades": [7, 6]
    }
}

# Función para calcular la utilidad esperada de una decisión
def utilidad_esperada(datos):
    utilidad_total = 0
    for probabilidad, utilidad in zip(datos["probabilidades"], datos["utilidades"]):
        utilidad_total += probabilidad * utilidad
    return utilidad_total

# Variables para guardar la mejor decisión
mejor_utilidad = float('-inf')  # Se empieza con la utilidad más baja posible
mejor_decision = ""

# Se evalúan todas las decisiones posibles
for decision, datos in decisiones.items():
    utilidad = utilidad_esperada(datos)
    print(f"Utilidad esperada para {decision}: {utilidad}")

    # Se actualiza si encontramos una mejor utilidad
    if utilidad > mejor_utilidad:
        mejor_utilidad = utilidad
        mejor_decision = decision

# Resultado final
print(f"\nLa mejor decisión es: '{mejor_decision}' con una utilidad esperada de {mejor_utilidad}")


