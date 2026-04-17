import heapq # Módulo para manejar colas de prioridad (min-heap)

def costo_uniforme(grafo, inicio, objetivo):
    """
    Encuentra el camino más barato considerando los pesos de las aristas.
    """
    # La cola de prioridad guardará tuplas: (costo_acumulado, camino)
    # Inicialmente, el costo es 0 y el camino solo tiene el nodo inicial.
    cola_prioridad = [(0, [inicio])]
    
    # Diccionario para guardar el menor costo encontrado para llegar a cada nodo.
    # Esto evita ciclos y reprocesamientos innecesarios.
    visitados = {}
    
    while cola_prioridad:
        # heapq.heappop siempre extrae la tupla con el MENOR costo_acumulado
        costo_actual, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]
        
        # Si llegamos al objetivo, al extraerlo de la cola de prioridad,
        # garantizamos que es el camino más barato posible.
        if nodo_actual == objetivo:
            print(f"UCS: Camino encontrado: {camino} con costo {costo_actual}")
            return camino, costo_actual
            
        # Si es la primera vez que visitamos el nodo, o si encontramos 
        # una forma más barata de llegar a él...
        if nodo_actual not in visitados or costo_actual < visitados[nodo_actual]:
            # Actualizamos el costo mínimo registrado para este nodo
            visitados[nodo_actual] = costo_actual
            
            # Exploramos sus vecinos (que ahora son un diccionario de {vecino: costo})
            for vecino, costo_arista in grafo[nodo_actual].items():
                nuevo_costo = costo_actual + costo_arista # Sumamos el costo
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                
                # Insertamos el nuevo camino en la cola de prioridad
                heapq.heappush(cola_prioridad, (nuevo_costo, nuevo_camino))
                
    print("UCS: No se encontró camino.")
    return None

if __name__ == "__main__":
    # Definimos un grafo de prueba con costos (grafo ponderado)
    grafo_costos = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3, 'G': 8},
        'D': {'B': 2},
        'E': {'B': 5, 'F': 1, 'G': 2},
        'F': {'C': 3, 'E': 1},
        'G': {'C': 8, 'E': 2}
    }
    
    # Prueba:
    print("Iniciando Búsqueda de Costo Uniforme de 'A' a 'G'...")
    costo_uniforme(grafo_costos, 'A', 'G')