# Imagen representada como una lista de listas
imagen = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Filtro de promedio (suavizado)
def aplicar_filtro(imagen):
    filas, columnas = len(imagen), len(imagen[0])
    imagen_suavizada = []
    
    for i in range(1, filas - 1):
        fila_suavizada = []
        for j in range(1, columnas - 1):
            # Calcular el promedio de los valores vecinos
            suma = sum([imagen[i-1][j-1], imagen[i-1][j], imagen[i-1][j+1],
                        imagen[i][j-1], imagen[i][j], imagen[i][j+1],
                        imagen[i+1][j-1], imagen[i+1][j], imagen[i+1][j+1]])
            promedio = suma // 9
            fila_suavizada.append(promedio)
        imagen_suavizada.append(fila_suavizada)
    
    return imagen_suavizada

# Aplicar filtro
imagen_suavizada = aplicar_filtro(imagen)

# Mostrar imagen suavizada
for fila in imagen_suavizada:
    print(" ".join(map(str, fila)))
