# Crear una imagen representada como una lista de listas
imagen = [["#" if (i + j) % 2 == 0 else "." for j in range(20)] for i in range(10)]

# Mostrar la imagen en consola
for fila in imagen:
    print(" ".join(fila))
