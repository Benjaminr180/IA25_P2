# Simulamos un conjunto de documentos
documentos = [
    "El perro corre por el parque.",
    "El gato juega con una pelota.",
    "La película de ayer fue emocionante.",
    "El perro y el gato son amigos.",
    "Me gusta ir al cine con mis amigos."
]

# Función para realizar la búsqueda de un término en los documentos
def recuperar_datos(termino):
    resultados = []
    for doc_id, doc in enumerate(documentos):
        if termino.lower() in doc.lower():
            resultados.append((doc_id, doc))
    return resultados

# Ejemplo de búsqueda
termino_busqueda = "perro"
resultados = recuperar_datos(termino_busqueda)

# Mostrar los resultados
if resultados:
    print(f"Se encontraron {len(resultados)} documentos con el término '{termino_busqueda}':")
    for doc_id, doc in resultados:
        print(f"Documento {doc_id}: {doc}")
else:
    print(f"No se encontraron documentos con el término '{termino_busqueda}'.")
