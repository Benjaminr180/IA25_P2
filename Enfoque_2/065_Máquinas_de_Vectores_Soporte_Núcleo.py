import random
import math

# Función para calcular la distancia euclidiana
def distancia_euclidiana(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

# Función de núcleo RBF
def kernel_rbf(x, y, gamma=0.1):
    return math.exp(-gamma * distancia_euclidiana(x, y) ** 2)

# Implementación de SVM
class SVM:
    def __init__(self, C=1.0, kernel=kernel_rbf):
        self.C = C
        self.kernel = kernel
        self.alpha = []
        self.b = 0
        self.support_vectors = []

    def fit(self, X, y):
        self.alpha = [random.random() for _ in range(len(X))]  # Inicializamos al azar
        # La optimización debe ir aquí, usando el método adecuado como el de secante o gradiente descendente
        # Por simplicidad, no realizamos la optimización completa, esto es solo un esquema básico

        # Aquí se usaría una optimización de tipo SMO (Sequential Minimal Optimization)
        # para encontrar los valores óptimos de 'alpha' y 'b'.
        pass

    def predict(self, X, X_train, y_train):
        predictions = []
        for x in X:
            prediction = sum(self.alpha[i] * y_train[i] * self.kernel(x, X_train[i]) for i in range(len(X_train))) + self.b
            predictions.append(1 if prediction >= 0 else -1)
        return predictions

    def decision_function(self, X, X_train, y_train):
        return [sum(self.alpha[i] * y_train[i] * self.kernel(x, X_train[i]) for i in range(len(X_train))) + self.b for x in X]

# Datos de ejemplo para clasificación (2D)
X_train = [
    [1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 7], [10, 12]
]
y_train = [1, 1, 1, -1, -1, -1, 1]  # Clases: 1 o -1

# Creamos el modelo SVM con núcleo RBF
svm = SVM(C=1.0, kernel=kernel_rbf)

# Entrenamos el modelo
svm.fit(X_train, y_train)

# Datos de prueba
X_test = [
    [5, 6], [7, 9]
]

# Hacemos predicciones
predicciones = svm.predict(X_test, X_train, y_train)
print(f"Predicciones para los puntos {X_test}: {predicciones}")
