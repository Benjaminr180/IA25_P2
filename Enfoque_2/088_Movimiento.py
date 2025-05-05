# Imagen representada como una lista de listas (escena 1)
imagen_1 = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Imagen representada como una lista de listas (escena 2 con movimiento)
imagen_2 = [
    [255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255],
    [255, 0, 255, 0, 255],
    [255, 0, 0, 0, 255],
    [255, 255, 255, 255, 255]
]

# Función para detectar movimiento comparando dos imágenes
def detectar_movimiento(imagen_1, imagen_2):
    filas, columnas = len(imagen_1), len(imagen_1[0])
    movimiento_detectado = []
    
    for i in range(filas):
        for j in range(columnas):
            if imagen_1[i][j] != imagen_2[i][j]:  # Detectar diferencia entre las imágenes
                movimiento_detectado.append((i, j))  # Guardamos la posición del movimiento
    
    return movimiento_detectado

# Detectar el movimiento entre las dos imágenes
movimiento = detectar_movimiento(imagen_1, imagen_2)

# Mostrar las posiciones donde se detectó movimiento
if movimiento:
    print("Movimiento detectado en las siguientes posiciones:")
    for posicion in movimiento:
        print(f"Posición: {posicion}")
else:
    print("No se detectó movimiento.")
