import random

# Función para crear un corpus de ejemplo
def crear_corpus():
    # Un corpus pequeño de ejemplo con frases
    corpus = [
        "el perro corre",
        "el gato duerme",
        "el perro duerme",
        "el gato corre",
        "el perro y el gato juegan"
    ]
    return corpus

# Función para construir un modelo probabilístico de un corpus
def modelo_probabilistico(corpus):
    # Contamos las ocurrencias de cada palabra
    frecuencia_palabras = {}
    total_palabras = 0
    
    for frase in corpus:
        palabras = frase.split()  # Dividimos la frase en palabras
        total_palabras += len(palabras)
        for palabra in palabras:
            if palabra in frecuencia_palabras:
                frecuencia_palabras[palabra] += 1
            else:
                frecuencia_palabras[palabra] = 1
                
    # Calculamos la probabilidad de cada palabra
    probabilidades = {palabra: frecuencia / total_palabras for palabra, frecuencia in frecuencia_palabras.items()}
    
    return probabilidades

# Función para generar una nueva frase usando el modelo probabilístico
def generar_frase(probabilidades, longitud_frase=5):
    palabras = list(probabilidades.keys())
    frase = []
    
    for _ in range(longitud_frase):
        palabra = random.choices(palabras, weights=probabilidades.values())[0]
        frase.append(palabra)
    
    return " ".join(frase)

# Crear el corpus
corpus = crear_corpus()

# Construir el modelo probabilístico
probabilidades = modelo_probabilistico(corpus)
print("Modelo Probabilístico (probabilidades de las palabras):")
print(probabilidades)

# Generar una nueva frase utilizando el modelo
frase_generada = generar_frase(probabilidades)
print("\nFrase generada aleatoriamente:")
print(frase_generada)
