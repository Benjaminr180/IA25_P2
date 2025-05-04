# Definimos una función para calcular la utilidad esperada
def utilidad_esperada(probabilidad, utilidad_si, utilidad_no):
    return probabilidad * utilidad_si + (1 - probabilidad) * utilidad_no

# Posibles decisiones
decisiones = ["Ir al parque", "Quedarse en casa"]

# Sin información del clima
utilidad_sin_info = {
    "Ir al parque": utilidad_esperada(0.7, 10, 0),   # 70% de buen clima, si llueve utilidad es 0
    "Quedarse en casa": 5  # Siempre utilidad 5
}

# Con información del clima: saber si llueve o no
# Si supiéramos con certeza que hay buen clima (probabilidad 1)
utilidad_con_info = {
    "Buen clima": {
        "Ir al parque": 10,
        "Quedarse en casa": 5
    },
    "Mal clima": {
        "Ir al parque": 0,
        "Quedarse en casa": 5
    }
}

# Probabilidades de los estados del clima
prob_buen_clima = 0.7
prob_mal_clima = 0.3

# Cálculo de la utilidad esperada si tuviéramos la información del clima
utilidad_info_total = (
    prob_buen_clima * max(utilidad_con_info["Buen clima"].values()) +
    prob_mal_clima * max(utilidad_con_info["Mal clima"].values())
)

# Cálculo de la mejor decisión sin pedir información
mejor_decision_sin_info = max(utilidad_sin_info, key=utilidad_sin_info.get)
mejor_utilidad_sin_info = utilidad_sin_info[mejor_decision_sin_info]

# Valor de la información (VOI)
valor_informacion = utilidad_info_total - mejor_utilidad_sin_info

# Resultados
print(f"Mejor decisión sin información: {mejor_decision_sin_info} con utilidad {mejor_utilidad_sin_info}")
print(f"Utilidad esperada si se obtiene información del clima: {utilidad_info_total}")
print(f"Valor de la información: {valor_informacion}")
