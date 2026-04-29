# 1. Definición del grafo
grafo = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E', 'G'], 'G': ['F']
}

# 2. Funciones del Algoritmo
def profundidad_limitada_aux(grafo, actual, objetivo, limite, camino_actual=None):
    """Función de apoyo que realiza la búsqueda con límite de profundidad."""
    if camino_actual is None: camino_actual = [actual]
    if actual == objetivo: return camino_actual
    if limite <= 0: return "Corte"
        
    corte_ocurrido = False
    for vecino in grafo[actual]:
        if vecino not in camino_actual:
            nuevo_camino = camino_actual + [vecino]
            resultado = profundidad_limitada_aux(grafo, vecino, objetivo, limite - 1, nuevo_camino)
            if resultado == "Corte": corte_ocurrido = True
            elif resultado is not None: return resultado
                
    return "Corte" if corte_ocurrido else None

def profundidad_iterativa(grafo, inicio, objetivo, limite_maximo=10):
    """Ejecuta búsquedas incrementando el límite poco a poco."""
    # Repite la búsqueda aumentando la profundidad permitida (0, 1, 2...)
    for profundidad in range(limite_maximo):
        resultado = profundidad_limitada_aux(grafo, inicio, objetivo, profundidad)
        
        if isinstance(resultado, list):
            print(f"IDDFS: Camino encontrado en profundidad {profundidad}: {resultado}")
            return resultado
        elif resultado is None:
            # Si retorna None (y no "Corte"), se exploró todo el grafo y no existe el objetivo
            break 
            
    print("IDDFS: Objetivo no encontrado o fuera del límite.")
    return None

# 3. Ejecución de prueba
print("--- Ejecutando Profundidad Iterativa ---")
profundidad_iterativa(grafo, 'A', 'G')