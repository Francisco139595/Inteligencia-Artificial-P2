import heapq

def greedy_best_first(grafo, inicio, objetivo, heuristica):
    """
    Algoritmo que expande el nodo que parece estar más cerca de la meta 
    según la función heurística h(n). Ignora el costo del camino recorrido.
    """
    # Cola de prioridad para seleccionar siempre el de menor valor heurístico
    # Estructura: (valor_h, nodo_actual, camino_seguido)
    frontera = [(heuristica[inicio], inicio, [inicio])]
    visitados = set()

    while frontera:
        # Extraemos el nodo con la h(n) más pequeña
        h, actual, camino = heapq.heappop(frontera)

        if actual == objetivo:
            return camino # Éxito: retornamos la ruta

        if actual not in visitados:
            visitados.add(actual)
            # Exploramos vecinos
            for vecino in grafo.get(actual, []):
                if vecino not in visitados:
                    # Solo nos importa la h del vecino para la prioridad
                    heapq.heappush(frontera, (heuristica[vecino], vecino, camino + [vecino]))
    
    return None # No se encontró camino

# Datos de prueba
grafo_ejemplo = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
h_ejemplo = {'A': 5, 'B': 2, 'C': 4, 'D': 0}
print(f"Ruta Voraz: {greedy_best_first(grafo_ejemplo, 'A', 'D', h_ejemplo)}")