# ==========================================
# 7. BÚSQUEDA EN GRAFOS (Patrón General)
# ==========================================

# 1. Definición del grafo independiente
grafo = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'F'],
    'D': ['B'], 
    'E': ['B', 'F'], 
    'F': ['C', 'E', 'G'], 
    'G': ['F']
}

# 2. Algoritmo
def busqueda_en_grafos(grafo, inicio, objetivo):
    """
    Plantilla base de la 'Búsqueda en Grafos'.
    Utiliza un conjunto de nodos 'explorados' para evitar ciclos infinitos.
    """
    # 'frontera' almacena los caminos descubiertos que aún no procesamos
    frontera = [[inicio]]
    
    # CONCEPTO CLAVE: Conjunto de nodos explorados
    explorados = set()
    
    while frontera:
        # Extraemos un camino de nuestra frontera
        camino = frontera.pop(0) 
        nodo_actual = camino[-1]
        
        # Prueba de objetivo: ¿Llegamos a la meta?
        if nodo_actual == objetivo:
            print(f"Búsqueda en Grafos -> Camino encontrado: {camino}")
            return camino
            
        # REGLA PRINCIPAL: Solo expandimos el nodo si NO ha sido explorado antes
        if nodo_actual not in explorados:
            # Lo marcamos como explorado inmediatamente para no volver a procesarlo
            explorados.add(nodo_actual) 
            
            # Generamos los vecinos (sucesores)
            for vecino in grafo[nodo_actual]:
                # Evitamos agregar a la frontera nodos que ya fueron explorados
                if vecino not in explorados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    frontera.append(nuevo_camino)
                    
    print("Búsqueda en Grafos -> No se encontró el objetivo.")
    return None

# 3. Ejecución de prueba
print("--- Ejecutando Búsqueda en Grafos ---")
busqueda_en_grafos(grafo, 'A', 'G')