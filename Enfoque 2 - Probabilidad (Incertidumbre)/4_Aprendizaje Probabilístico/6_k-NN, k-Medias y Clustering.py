import numpy as np
from typing import Tuple

def k_means(puntos: np.ndarray, k: int, max_iter: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """
    Algoritmo de agrupamiento no supervisado K-Medias (K-Means).
    Busca dividir un conjunto de puntos N-dimensionales en 'k' grupos (clusters)
    minimizando la varianza dentro de cada grupo.
    """
    print(f"--- Iniciando K-Means (k={k}) ---")
    print(f"Puntos a agrupar:\n{puntos}\n")

    # 1. Inicializar centroides aleatorios (seleccionando 'k' puntos al azar)
    indices_aleatorios = np.random.choice(len(puntos), k, replace=False)
    centroides = puntos[indices_aleatorios]
    print(f"-> Centroides iniciales aleatorios:\n{centroides}\n")
    
    etiquetas = np.zeros(len(puntos))
    
    for iteracion in range(max_iter):
        print(f"--- Iteración {iteracion + 1} ---")
        
        # 2. Asignar puntos al centroide más cercano (Paso de Expectativa)
        # Calculamos la distancia euclidiana de cada punto a cada centroide
        distancias = np.linalg.norm(puntos[:, np.newaxis] - centroides, axis=2)
        etiquetas = np.argmin(distancias, axis=1)
        print(f"  -> Asignación de grupos (etiquetas): {etiquetas}")
        
        # 3. Actualizar centroides a la media de sus puntos (Paso de Maximización)
        nuevos_centroides = []
        for i in range(k):
            puntos_cluster = puntos[etiquetas == i]
            # Si un grupo se queda sin puntos, mantenemos su centroide anterior para evitar divisiones por cero (NaN)
            if len(puntos_cluster) > 0:
                nuevos_centroides.append(puntos_cluster.mean(axis=0))
            else:
                nuevos_centroides.append(centroides[i])
                
        nuevos_centroides = np.array(nuevos_centroides)
        print(f"  -> Nuevos centroides calculados:\n{nuevos_centroides}\n")
        
        # Condición de convergencia: si los centroides no cambian, terminamos
        if np.allclose(centroides, nuevos_centroides):
            print("-> Convergencia alcanzada: Los centroides han dejado de moverse.")
            break
            
        centroides = nuevos_centroides
            
    return centroides, etiquetas

# Datos de prueba (2D): 2 grupos de puntos claramente separados
datos = np.array([[1.0, 1.0], [1.0, 2.0], [8.0, 8.0], [8.0, 9.0], [1.5, 1.5], [8.5, 8.5]])
centros, etiq = k_means(datos, k=2)