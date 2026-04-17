def busqueda_en_profundidad(grafo, inicio, objetivo):
    """
    Implementación iterativa usando una pila (stack).
    """
    # La pila guardará los caminos. Una lista en Python funciona como pila
    # usando los métodos .append() y .pop().
    pila = [[inicio]]
    visitados = set()
    
    while pila:
        # Extraemos el ÚLTIMO elemento añadido a la pila (LIFO)
        camino = pila.pop()
        nodo_actual = camino[-1]
        
        if nodo_actual == objetivo:
            print(f"DFS: Camino encontrado: {camino}")
            return camino
            
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            # Recorremos los vecinos. (A menudo se invierte el orden para 
            # explorar de izquierda a derecha, pero no es estrictamente necesario)
            for vecino in reversed(grafo[nodo_actual]):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    pila.append(nuevo_camino) # Lo ponemos encima de la pila
                    
    print("DFS: No se encontró camino.")
    return None

if __name__ == "__main__":
    # Definimos el grafo estándar de prueba (sin pesos)
    grafo_estandar = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C'],
        'G': ['C']
    }
    
    # Prueba:
    print("Iniciando Búsqueda en Profundidad (DFS) de 'A' a 'G'...")
    busqueda_en_profundidad(grafo_estandar, 'A', 'G')