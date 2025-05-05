# Imagen representada como una lista de listas
imagen = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Análisis de gradiente simple (diferencia entre píxeles adyacentes)
def analizar_gradiente(imagen):
    filas, columnas = len(imagen), len(imagen[0])
    imagen_gradiente = []
    
    for i in range(filas):
        fila_gradiente = []
        for j in range(columnas - 1):
            # Calcular la diferencia entre píxeles adyacentes
            gradiente = abs(imagen[i][j+1] - imagen[i][j])
            fila_gradiente.append(gradiente)
        imagen_gradiente.append(fila_gradiente)
    
    return imagen_gradiente

# Aplicar análisis de gradiente
imagen_gradiente = analizar_gradiente(imagen)

# Mostrar imagen con gradiente
for fila in imagen_gradiente:
    print(" ".join(map(str, fila)))
