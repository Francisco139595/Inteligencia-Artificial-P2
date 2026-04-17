def profundidad_limitada(grafo, actual, objetivo, limite, camino_actual=None):
    """
    Implementación recursiva. Detiene la exploración si se alcanza el 'limite'.
    """
    # Inicialización del camino en la primera llamada
    if camino_actual is None:
        camino_actual = [actual]
        
    # Caso base 1: Hemos encontrado el objetivo
    if actual == objetivo:
        return camino_actual
        
    # Caso base 2: Se alcanzó el límite de profundidad, no podemos seguir bajando
    if limite <= 0:
        return "Corte" # Retornamos un indicador de que nos detuvimos por el límite
        
    corte_ocurrido = False
    
    # Exploramos los vecinos
    for vecino in grafo[actual]:
        # Evitamos ciclos simples en el camino actual
        if vecino not in camino_actual:
            nuevo_camino = camino_actual + [vecino]
            # Llamada recursiva disminuyendo el límite en 1
            resultado = profundidad_limitada(grafo, vecino, objetivo, limite - 1, nuevo_camino)
            
            if resultado == "Corte":
                corte_ocurrido = True # Registramos que al menos una rama fue cortada
            elif resultado is not None:
                return resultado # Encontramos el objetivo en una de las ramas
                
    # Si hubo cortes y no encontramos el objetivo, retornamos "Corte"
    if corte_ocurrido:
        return "Corte"
    return None # No se encontró nada y no hubo cortes (exploración exhaustiva fallida)

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
    limite = 3
    print(f"Iniciando Búsqueda en Profundidad Limitada de 'A' a 'G' con límite {limite}...")
    resultado_dls = profundidad_limitada(grafo_estandar, 'A', 'G', limite)
    print(f"DLS (Límite {limite}): {resultado_dls}")