import heapq

def a_star(grafo, inicio, objetivo, heuristica):
    """
    Busca el camino más corto combinando el costo real g(n) 
    y el costo estimado h(n). f(n) = g(n) + h(n).
    """
    # Prioridad basada en f(n) = g + h
    # (f_total, g_acumulado, nodo, camino)
    cola = [(heuristica[inicio], 0, inicio, [inicio])]
    distancias_minimas = {inicio: 0}

    while cola:
        f, g, actual, camino = heapq.heappop(cola)

        if actual == objetivo:
            return camino

        for vecino, costo_arco in grafo.get(actual, []):
            nuevo_g = g + costo_arco
            
            # Si encontramos un camino más corto a este vecino, lo actualizamos
            if vecino not in distancias_minimas or nuevo_g < distancias_minimas[vecino]:
                distancias_minimas[vecino] = nuevo_g
                f_nuevo = nuevo_g + heuristica[vecino]
                heapq.heappush(cola, (f_nuevo, nuevo_g, vecino, camino + [vecino]))
                
    return None

# Grafo con pesos: {origen: [(destino, costo)]}
grafo_pesos = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}
h_valores = {'A': 3, 'B': 4, 'C': 1, 'D': 0}
print(f"Ruta A*: {a_star(grafo_pesos, 'A', 'D', h_valores)}")
print(f"Ruta B*: {a_star(grafo_pesos, 'B', 'D', h_valores)}")
print(f"Ruta C*: {a_star(grafo_pesos, 'C', 'D', h_valores)}")