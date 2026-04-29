from collections import deque

def busqueda_en_anchura(grafo, inicio):
    # Conjunto para mantener un registro de los nodos visitados y evitar caer en ciclos infinitos
    visitados = set()
    # Cola (deque) para procesar los nodos en orden FIFO (Primero en entrar, primero en salir)
    cola = deque([inicio])
    visitados.add(inicio)
    
    # Lista para almacenar y retornar el orden en que se visitan los nodos
    resultado = []
    
    while cola:
        nodo_actual = cola.popleft() # Se saca el primer nodo de la cola para explorarlo
        resultado.append(nodo_actual)
        
        # Se exploran todos los vecinos directos del nodo actual
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino) # Se marca el vecino como visitado
                cola.append(vecino)   # Se añade al final de la cola para procesarlo después
                
    return resultado

def busqueda_en_profundidad(grafo, inicio):
    visitados = set()
    pila = [inicio] # Usamos una lista convencional a modo de pila (LIFO: Último en entrar, primero en salir)
    resultado = []
    
    while pila:
        nodo_actual = pila.pop() # Sacamos el último elemento que entró en la pila
        if nodo_actual not in visitados:
            visitados.add(nodo_actual) # Se marca el nodo actual como visitado
            resultado.append(nodo_actual)
            
            # Invertimos los vecinos para mantener el mismo orden de lectura de izquierda a derecha
            for vecino in reversed(grafo.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append(vecino) # Se agregan los vecinos no visitados a la cima de la pila
                    
    return resultado

def encontrar_camino_mas_corto(grafo, inicio, objetivo):
    visitados = set()
    # La cola ahora guarda tuplas con dos elementos: (nodo_actual, camino_recorrido_hasta_el_momento)
    cola = deque([(inicio, [inicio])])
    visitados.add(inicio)
    
    while cola:
        nodo_actual, camino = cola.popleft()
        
        # Si el nodo actual es el que estamos buscando, retornamos el camino acumulado hasta ahí
        if nodo_actual == objetivo:
            return camino
            
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                # Agregamos el vecino a la cola y le sumamos el nuevo paso al camino recorrido
                cola.append((vecino, camino + [vecino]))
                
    return None

def main():
    # Ejemplo de un grafo representado como lista de adyacencia
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Ejecuta el algoritmo BFS y muestra el resultado en la consola
    print("Recorrido BFS empezando desde el nodo 'A':")
    recorrido = busqueda_en_anchura(grafo, 'A')
    print(recorrido)
    
    # Ejecuta el algoritmo DFS y muestra el resultado en la consola
    print("\nRecorrido DFS empezando desde el nodo 'A':")
    recorrido_dfs = busqueda_en_profundidad(grafo, 'A')
    print(recorrido_dfs)
    
    # Busca el camino más corto entre el nodo A y F utilizando la adaptación de BFS
    print("\nCamino más corto de 'A' a 'F' (usando BFS):")
    camino = encontrar_camino_mas_corto(grafo, 'A', 'F')
    print(camino)

if __name__ == "__main__":
    main()
