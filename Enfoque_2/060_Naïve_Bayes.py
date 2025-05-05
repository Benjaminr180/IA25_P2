# Datos de entrenamiento (simplificados)
datos = [
    {"clima": "soleado", "jugar": "no"},
    {"clima": "nublado", "jugar": "sí"},
    {"clima": "lluvioso", "jugar": "sí"},
    {"clima": "soleado", "jugar": "no"},
    {"clima": "nublado", "jugar": "sí"},
    {"clima": "lluvioso", "jugar": "no"},
    {"clima": "soleado", "jugar": "sí"},
]

# Contadores para cálculo de probabilidad
from collections import Counter

# Paso 1: Calcular P(jugar = sí) y P(jugar = no)
conteo_jugar = Counter(d["jugar"] for d in datos)
total = len(datos)

P_si = conteo_jugar["sí"] / total
P_no = conteo_jugar["no"] / total

# Paso 2: Calcular P(clima | jugar)
def contar_condicional(clima_objetivo, jugar_objetivo):
    return sum(1 for d in datos if d["clima"] == clima_objetivo and d["jugar"] == jugar_objetivo)

clima_test = "nublado"

P_clima_dado_si = contar_condicional(clima_test, "sí") / conteo_jugar["sí"]
P_clima_dado_no = contar_condicional(clima_test, "no") / conteo_jugar["no"]

# Paso 3: Aplicar Bayes (sin normalizar)
prob_si = P_clima_dado_si * P_si
prob_no = P_clima_dado_no * P_no

# Normalizar
total_prob = prob_si + prob_no
prob_si_final = prob_si / total_prob
prob_no_final = prob_no / total_prob

# Resultado
print(" Clasificación Naïve Bayes:")
print(f"Probabilidad de jugar: {prob_si_final:.2f}")
print(f"Probabilidad de NO jugar: {prob_no_final:.2f}")
