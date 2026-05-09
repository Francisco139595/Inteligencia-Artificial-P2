from typing import List, Dict

def clustering_no_supervisado(datos: List[float], k: int = 2, iteraciones: int = 3) -> Dict[int, List[float]]:
    """
    A diferencia del aprendizaje supervisado, aquí no hay etiquetas.
    El algoritmo busca estructuras o patrones intrínsecos en los datos.
    
    Ejemplo simulado con K-Means (1D):
    1. Asigna centroides iniciales.
    2. Agrupa cada dato a su centroide más cercano.
    3. Recalcula el centroide como el promedio del grupo.
    """
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")
        
    print("--- Iniciando Agrupamiento No Supervisado (Clustering) ---")
    print(f"Datos originales sin etiquetar: {datos}\n")
    
    # Inicialización simple: tomamos los primeros 'k' elementos como centroides
    centroides = datos[:k] 
    clusters = {}
    
    for i in range(iteraciones):
        print(f"--- Iteración {i+1} ---")
        
        # Paso 1: Asignación (Agrupar por cercanía al centroide)
        clusters = {j: [] for j in range(k)}
        for x in datos:
            distancias = [abs(x - c) for c in centroides]
            cluster_cercano = distancias.index(min(distancias))
            clusters[cluster_cercano].append(x)
            
        print(f"  -> Grupos formados: {clusters}")
        
        # Paso 2: Actualización de centroides (Mover el centroide al medio del grupo)
        nuevos_centroides = []
        for j in range(k):
            nuevo_c = sum(clusters[j]) / len(clusters[j]) if clusters[j] else centroides[j]
            nuevos_centroides.append(nuevo_c)
            
        print(f"  -> Nuevos centroides: {[round(c, 2) for c in nuevos_centroides]}\n")
        centroides = nuevos_centroides
        
    print("-> Clustering Finalizado. Patrones intrínsecos descubiertos.")
    return clusters

datos_ejemplo = [1.0, 2.0, 1.5, 8.0, 9.0, 8.5]
clustering_no_supervisado(datos_ejemplo, k=2)