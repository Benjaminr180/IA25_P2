# Imagen representada como una lista de listas (contornos simples)
imagen = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Detectar "contornos" como diferencias entre los píxeles
def detectar_contornos(imagen):
    filas, columnas = len(imagen), len(imagen[0])
    contornos = []
    
    for i in range(1, filas - 1):
        fila_contornos = []
        for j in range(1, columnas - 1):
            # Si el píxel tiene una diferencia significativa con el vecino
            if abs(imagen[i][j] - imagen[i-1][j]) > 50 or abs(imagen[i][j] - imagen[i+1][j]) > 50:
                fila_contornos.append(255)  # Detectamos el borde
            else:
                fila_contornos.append(0)
        contornos.append(fila_contornos)
    
    return contornos

# Aplicar detección de contornos
imagen_contornos = detectar_contornos(imagen)

# Mostrar contornos detectados
for fila in imagen_contornos:
    print(" ".join(map(str, fila)))
