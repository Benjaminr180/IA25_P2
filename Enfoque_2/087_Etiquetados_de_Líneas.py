# Imagen representada como una lista de listas
imagen = [
    [0, 0, 0, 0, 0],
    [0, 255, 255, 0, 0],
    [0, 255, 255, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Etiquetado simple de líneas (diferencia de intensidad)
def etiquetar_lineas(imagen):
    filas, columnas = len(imagen), len(imagen[0])
    lineas = []
    
    for i in range(filas):
        for j in range(columnas - 1):
            if abs(imagen[i][j] - imagen[i][j+1]) > 50:  # Cambios significativos
                lineas.append((i, j))
    
    return lineas

# Obtener las líneas detectadas
lineas_detectadas = etiquetar_lineas(imagen)

# Mostrar las líneas detectadas
for linea in lineas_detectadas:
    print(f"Línea detectada en la posición: {linea}")
