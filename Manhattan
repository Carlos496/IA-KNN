from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Datos de entrenamiento
X = np.array([
    [2, 0],  # Caso 1
    [4, 4],  # Caso 2
    [1, 1],  # Caso 3
    [2, 4],  # Caso 4
    [2, 2],  # Caso 5
    [2, 3],  # Caso 6
    [3, 4],  # Caso 7
    [3, 3]   # Caso 8
])

y = np.array([0, 1, 0, 1, 0, 1, 0, 1])  # Clases correspondientes

# Crear el clasificador k-NN con k=1 y distancia Manhattan (p=1)
knn = KNeighborsClassifier(n_neighbors=1, p=1)  # p=1 para distancia Manhattan
knn.fit(X, y)

# Punto a clasificar
nuevo_punto = np.array([[2.5, 2.5]])
# Realizar la predicción
clase_predicha = knn.predict(nuevo_punto)

print(f"El punto {nuevo_punto[0]} se clasifica como: {clase_predicha[0]}")
