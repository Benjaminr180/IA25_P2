# Imagen representada como una lista de listas
imagen = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Filtro Sobel simplificado para detectar bordes en una dirección
def aplicar_sobel(imagen):
    filas, columnas = len(imagen), len(imagen[0])
    imagen_sobel = []
    
    for i in range(1, filas - 1):
        fila_sobel = []
        for j in range(1, columnas - 1):
            # Aplicamos un filtro Sobel simple en una dirección (por ejemplo, horizontal)
            gx = imagen[i-1][j+1] + 2*imagen[i][j+1] + imagen[i+1][j+1] - imagen[i-1][j-1] - 2*imagen[i][j-1] - imagen[i+1][j-1]
            fila_sobel.append(abs(gx))  # Valor absoluto para resaltar los bordes
        imagen_sobel.append(fila_sobel)
    
    return imagen_sobel

# Aplicar el filtro Sobel
imagen_sobel = aplicar_sobel(imagen)

# Mostrar imagen con bordes detectados
for fila in imagen_sobel:
    print(" ".join(map(str, fila)))
