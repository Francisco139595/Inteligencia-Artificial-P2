from collections import deque

# 1. Definición del grafo
grafo = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E', 'G'], 'G': ['F']
}

# 2. Algoritmo
def busqueda_bidireccional(grafo, inicio, objetivo):
    """Lanza dos BFS al mismo tiempo: uno desde el inicio y otro desde la meta."""
    if inicio == objetivo: return [inicio]
        
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])
    
    # Diccionarios para recordar caminos {nodo_visitado: camino_para_llegar_a_el}
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}
    
    while cola_inicio and cola_objetivo:
        # -- 1. Expandir un nivel desde el inicio --
        camino_i = cola_inicio.popleft()
        nodo_i = camino_i[-1]
        
        for vecino in grafo[nodo_i]:
            if vecino not in visitados_inicio:
                nuevo_camino = camino_i + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)
                
                # ¡Choque frontal! La búsqueda inversa ya había llegado aquí
                if vecino in visitados_objetivo:
                    camino_final = nuevo_camino + visitados_objetivo[vecino][::-1][1:]
                    print(f"Bidireccional: Encontrado chocando en '{vecino}': {camino_final}")
                    return camino_final

        # -- 2. Expandir un nivel desde el objetivo (hacia atrás) --
        camino_o = cola_objetivo.popleft()
        nodo_o = camino_o[-1]
        
        for vecino in grafo[nodo_o]:
            if vecino not in visitados_objetivo:
                nuevo_camino = camino_o + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)
                
                # ¡Choque frontal! La búsqueda de inicio ya había llegado aquí
                if vecino in visitados_inicio:
                    camino_final = visitados_inicio[vecino] + nuevo_camino[::-1][1:]
                    print(f"Bidireccional: Encontrado chocando en '{vecino}': {camino_final}")
                    return camino_final

    print("Bidireccional: No se encontró camino.")
    return None

# 3. Ejecución de prueba
print("--- Ejecutando Búsqueda Bidireccional ---")
busqueda_bidireccional(grafo, 'A', 'G')